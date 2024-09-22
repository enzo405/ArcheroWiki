import re
import time
import json

start_time = time.time()  # Start the timer


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
    return build_sentence_list


def translate(msgid, glossary):
    msgid_build = build(msgid.lower())
    i_msgid = 0
    for k, v in msgid_build.items():
        try:
            translated_text = glossary[v]
            if k == 3:
                translated_text = f"{translated_text}."
            elif k == 4:
                translated_text = f"{translated_text}:"
            elif k == 6:
                translated_text = f"{translated_text}?"
            return translated_text
        except:
            i_msgid += 1
    raise Exception("No translation found")


# Put the targetted language code
lang_code_filedir = "de"  # 'de' | 'fr' | 'br' | 'ru'
HandMadeGlossaryOfficialTranslation = makeOfficialTranslationDict(
    lang_code_filedir if lang_code_filedir != "br" else "PT_BR"
)

with open(
    f"web-project/locale/{lang_code_filedir}/LC_MESSAGES/django.po",
    "r",
    encoding="utf-8",
) as f:
    content = f.read()

# Regular expression pattern to match msgid and msgstr lines
pattern = re.compile(r'msgid "(.*?)"\s+msgstr "(.*?)"', re.DOTALL)

# Find all matches in the content
matches = pattern.findall(content)

# Dictionary to store msgid and msgstr pairs
msgid_msgstr_dict = {}
for match in matches:
    msgid = match[0]
    msgstr = match[1]
    msgid_msgstr_dict[msgid] = msgstr

# Update the original content with translations
updated_content = content
translations = {}  # Store translations as a dictionary
translated_sentence = 0

for msgid in msgid_msgstr_dict:
    try:
        if msgid in msgid_msgstr_dict and msgid != "":
            translated_text = translate(msgid, HandMadeGlossaryOfficialTranslation)
            translated_sentence += 1
            updated_content = updated_content.replace(
                f'msgid "{msgid}"\nmsgstr "{msgid_msgstr_dict[msgid]}"',
                f'msgid "{msgid}"\nmsgstr "{translated_text}"',
            )
            translations[msgid] = translated_text
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
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")
print(f"Sentence translated with HABBY wording: {translated_sentence}")
