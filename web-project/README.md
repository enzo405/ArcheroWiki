# Contact me
- [Reddit](https://www.reddit.com/user/LuhCaran101/)
- [Discord](https://discord.com/users/382930544385851392)


# Beginner / Not a Programmer

If you're a beginner or not into coding, i don't suggest you to add features, or let me know if you really want to add something.

**Updating wiki's content**
- Text: What is doable for a random person is just updating the wiki content which is inside this file : [wiki_data.py](./calculator/data/wiki_data.py), and if you have trouble, you can ask chatGPT for help (or me 😀)
- Image: all the images are in the following directory ./web-project/calculator/static/image/ (if you want Archero ingame's image, you can ask on the official discord, someone will give it to you, or ask me directly)


# TODO :

- Make a REST Api for making CRUD action on the content (items, heroes, skills, articles, wiki guides & tierlists etc...):
  - Might need to remove translation to be able to edit the [text json file](./calculator/data/wiki_data.py)

- Be able to update the images using file upload (basically an api)

- Put the archero wiki content in the database ?

- Having a searchbar in the header to search content in the whole wiki

- Enhance google CEO for better referencement

- Fix damage calculator (route = `/wiki/damage-calculator/`)
    - needs to know the ingame damage formula (reverse engineering, let me know at this point, i've done lots of research for this)

- If there's an easy way to update wiki's content (API), then add Dragons, Glyphs, etc...

- Refactor the wiki 😂😂 (because the code is really bad i know xD)
    - at least the database 😂😂😂 (i'm ashamed to leave it like this ngl)

- Better login system ? get rid of cookies (at least the way i've done it)


If you have any other ideas, please let me know through issues on github.


# Translation files

**Let me know before so i can ask habby ingame Archero's Translations (you can see the 6.1.3 version [here](./calculator/static/json/Archero_Translation.json))**

### Command for translations :

**Reads all files and generate .po files**
> [e.g french translation file](./locale/fr/LC_MESSAGES/django.po)
```bash
python .\manage.py makemessages --all --no-wrap --no-obsolete
```
Since this might affect already existing translation, i have made some scripts to read the .po file and edit it correctly and avoid going through the 40k line of translation.


**Reads .po files and compile it**
```bash
python .\manage.py compilemessages --ignore=env
```


# Usefull links:

**Png to Svg Converter:**
https://onlineconvertfree.com/convert/png/

**Edit image :**
https://pixlr.com/

**Documentation django-admin/#django-admin-makemessages**
https://docs.djangoproject.com/en/4.2/ref/django-admin/#django-admin-makemessages

**ChatGPT**
https://chatgpt.com/