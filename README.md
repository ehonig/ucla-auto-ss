# ucla-auto-ss
Automatically[^1] complete UCLA's daily symptom monitoring survey

[^1]: Excluding DUO authentication, which we should definitely not automate.

## Installation:

1. Download this directory (e.g. `git clone https://github.com/ehonig/ucla-auto-ss.git`)
2. Download the proper chromedriver from https://chromedriver.chromium.org/downloads; there's a guide to choosing the right version on the website
3. Create a virtual environment and install packages from `requirements.txt` (e.g. `pip install -r requirements.txt`)
4. Run `python init.py`
5. Test `python auto_symptom_survey.py` to see if it works

Steps 4 and 5 are assumed to be ran from a shell inside the directory, with the virtual environment created in Step 3 activated.

Don't use this if you have symptoms.

I may or may not add more details someday.

TODO:
- [x] add instructions on obtaining `chromedriver`
- [x] create `init.py` for first-time initialization
- [ ] explain how to create a virtual environment
- [ ] create conda environment YML file
- [ ] explain how to create a script
- [ ] explain how to create a job for automatically running the script
