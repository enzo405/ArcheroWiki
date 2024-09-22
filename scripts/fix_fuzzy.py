import re
import time
import json

start_time = time.time()  # Start the timer
PUT_EMPTY_STRING_FOR_MISSING_TRANSLATION = True
LANG = "br"

lvlTranslated = {"en": "Lvl", "fr": "Niv.", "de": "Lvl", "br": "Nível", "ru": "Уровни"}


def makeOfficialTranslationDict(language="en") -> dict:
    result_dict = {}
    with open(
        "web-project\calculator\static\json\Archero_Translation.json",
        "r",
        encoding="utf-8",
    ) as f:
        ArcheroOfficialDataTranslation = json.load(f)
    for sentence in ArcheroOfficialDataTranslation["language"]:
        try:
            result_dict.update(
                {sentence["EN"].lower(): sentence[str(language).upper()]}
            )
        except (KeyError, TypeError):
            pass
    return result_dict


def remove_bracketed_text(string) -> list:
    try:
        pattern = re.compile(
            r"\[(?!x\]|\bMajor\b|\bMinor\b)[^\]]*\]"
        )  # except +[x] and [Major] and [Minor]
        removed_texts = pattern.findall(string)
        result = pattern.sub("", string).strip()
        removed_text = ", ".join(removed_texts).strip()
        return [result, removed_text]
    except:
        return [string, ""]


def remove_value_int(string) -> list:
    try:
        pattern = re.compile(r"(\+\d+|\+\d+%|\+\[\w+\]%)$")
        if pattern.search(string):
            removed_text = pattern.findall(string)[0]
            result = pattern.sub("", string).strip()
        else:
            removed_text = ""
            result = string

        return [result, removed_text]
    except:
        return [string, []]


def rebuild_bracketed_text(result_translated, removed_text, glossary, k) -> str:
    """ "
    e.g:
        result_translated = "Augmente les dégâts de mêlée"
        removed_text = "[Mythic]"
        glossary = {"mythic": "Mythique"}

    Wanted result: "[Mythique] Augmente les dégâts de mêlée"
    """
    try:
        bracket_text = removed_text.replace("[", "").replace("]", "")
        translated_bracket_text = glossary[
            bracket_text.lower().replace("+1", "").replace("+2", "").replace("+3", "")
        ]
        if "+" in bracket_text:
            translated_bracket_text = (
                f"{translated_bracket_text} +{bracket_text.split('+')[1]} "
            )

        # TODO be careful if the bracket position is not at the begining, at the time i did this, there was no sentence other than at the begining
        return f"[{translated_bracket_text}] {result_translated}"
    except Exception:
        if "Lvl" in bracket_text:
            return f"[{bracket_text.replace('Lvl', lvlTranslated[lang_code_filedir])}] {result_translated}"
        elif k == 8:
            return result_translated


def rebuild_value_int(translated_text, removed_text, msgid) -> str:
    result = f"{translated_text} {removed_text}" if removed_text else translated_text
    return result


def build(string) -> dict:
    build_sentence_list = {}
    build_sentence_list.update({0: string})
    (
        build_sentence_list.update({1: string[:-1]})
        if string[-1] in [":", ";", "!", "?", ",", ".", "%", ""]
        else ""
    )
    build_sentence_list.update({2: f"{string} "})
    build_sentence_list.update({3: f"{string}."})
    build_sentence_list.update({4: f"{string}:"})
    build_sentence_list.update({5: f"{string}!"})
    build_sentence_list.update({6: f"{string}?"})
    string_without_bracket = remove_bracketed_text(string)[0]
    build_sentence_list.update({7: string_without_bracket})
    build_sentence_list.update({8: remove_value_int(string_without_bracket)[0]})
    return build_sentence_list


def translate(msgid, glossary):
    msgid_build = build(msgid.lower())
    for k, v in msgid_build.items():
        try:
            translated_text = glossary[v]  # throws KeyError if not found
            if k == 3:
                translated_text = f"{translated_text}."
            elif k == 4:
                translated_text = f"{translated_text}:"
            elif k == 6:
                translated_text = f"{translated_text}?"
            elif k == 7:
                translated_text = rebuild_bracketed_text(
                    translated_text, remove_bracketed_text(msgid)[1], glossary, k
                )
            elif k == 8:
                rebuilded_bracketed_text = rebuild_bracketed_text(
                    translated_text, remove_bracketed_text(msgid)[1], glossary, k
                )
                translated_text = rebuild_value_int(
                    rebuilded_bracketed_text, remove_value_int(msgid)[1], msgid
                )
            return translated_text
        except KeyError:
            pass
        except Exception as e:
            print(f"Error: {e} -> {v}")
    if PUT_EMPTY_STRING_FOR_MISSING_TRANSLATION:
        return ""
    else:
        raise Exception(f'No translation found for "{msgid}"')


# Set the target language code
lang_code_filedir = LANG  # 'de' | 'fr' | 'br' | 'ru'
HandMadeGlossaryOfficialTranslation = makeOfficialTranslationDict(
    lang_code_filedir if lang_code_filedir != "br" else "PT_BR"
)

with open(
    f"web-project/locale/{lang_code_filedir}/LC_MESSAGES/django.po",
    "r",
    encoding="utf-8",
) as f:
    content = f.read()

# Regular expression pattern to match fuzzy translations with msgid and msgstr lines
fuzzy_pattern = re.compile(
    r'(#, fuzzy\n#\| msgid "(.*?)"\nmsgid "(.*?)"\nmsgstr "(.*?)")', re.DOTALL
)

# Find all fuzzy matches in the content
fuzzy_matches = fuzzy_pattern.findall(content)

# Update the original content with translations
updated_content = content
translations = {}  # Store translations as a dictionary
translated_sentence = 0

for match in fuzzy_matches:
    full_match = match[0]  # The entire fuzzy match
    original_msgid = match[1]  # The previous msgid (if exists)
    msgid = match[2]  # The current msgid
    msgstr = match[3]  # The current msgstr
    try:
        if msgid:
            translated_text = translate(msgid, HandMadeGlossaryOfficialTranslation)
            translated_sentence += 1
            # Replace the entire fuzzy match with the updated translation
            updated_content = updated_content.replace(
                full_match, f'msgid "{msgid}"\nmsgstr "{translated_text}"'
            )
    except Exception as e:
        pass

# Write the updated content back to the file
with open(
    f"web-project/locale/{lang_code_filedir}/LC_MESSAGES/django.po",
    "w",
    encoding="utf-8",
) as f:
    f.write(updated_content)

end_time = time.time()  # Stop the timer
elapsed_time = time.time() - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
print(f"Sentence translated with HABBY wording: {translated_sentence}")
