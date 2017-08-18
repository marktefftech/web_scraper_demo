# Web Scraper Demo

Selenium with Python Web Scraper Demo

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

1. A virtual environment (suggested but not required)
2. Chrome Driver: https://chromedriver.storage.googleapis.com/index.html?path=2.31/
  a. Download the correct version for your os
  b. unzip
  c. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin
    i. For Windows, see documentation: https://selenium-python.readthedocs.io/installation.html#detailed-instructions-for-windows-users
3. Install Selenium:
  a. You can simply install Selenium using pip

```
pip install selenium
```

  b. Alternativaly, you can install Selenium via the requirements.txt file (after cloning or downloading this repo).

```
pip install -r requirements.txt
```

### Installing

Once the prerequisites are meet and the repo is cloned or downloaded, simply run the script to see it work.

```
python3 myb_scraper.py
```

The end result will be 3 new csv files that contain the product names and their prices.

## Built With

* [Selenium](http://www.seleniumhq.org/) - Browser Automation

## Authors

* **Michael Delgado** - *Initial work* - [mike-del](https://github.com/mike-del)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* All the tutorials that helped me along the way. Thank you!
