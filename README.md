# Automatically Complete the UCLA Symptom Survey
Automatically[^1] complete UCLA's daily symptom monitoring survey

[^1]: Excluding DUO authentication, which we should definitely not automate.

## Installation:

1. Download this directory (e.g. `git clone https://github.com/ehonig/ucla-auto-ss.git`)
2. Download the proper chromedriver from https://chromedriver.chromium.org/downloads; there's a guide to choosing the right version on the website
3. If using conda, run `conda env create -f environment.yml`. Otherwise, create a virtual environment named "auto-symptom-survey" install the packages in `requirements.txt` using `pip install -r requirements.txt`.
4. Activate the virtual environment (for example: `conda activate auto-symptom-survey`)
5. Run `python init.py` and follow the instructions.

## Use

Now everything is setup properly; after activating the virtual environment, try running `python auto_symptom_survey.py`. You should see a Chrome browser open and the symptom survey be automatically completed for you[^1].

Steps 4 and 5 are assumed to be ran from a shell inside the directory, with the virtual environment created in Step 3 activated.

## Comments

Don't use this if you have symptoms.

I may or may not add more details someday.

---

TODO:
- [x] add instructions on obtaining `chromedriver`
- [x] create `init.py` for first-time initialization
- [x] create conda environment YML file
- [ ] explain how to create a virtual environment
- [ ] explain how to create a script
- [ ] explain how to create a job for automatically running the script
