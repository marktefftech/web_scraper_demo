# Web Scraper Demo
### Demo Video: [Watch here on Youtube](https://youtu.be/5Hsv9RZg09Q)

This is a quick tutorial on how to use Selenium with Python to create web scraper. The web scraper will pull up a website and record product information and price. You can use my script to run on your own computer. Then improve it to best meet your project needs. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

1. A virtual environment (suggested but not required)
2. [Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=2.31/)
- Download the correct version for your os
- unzip
- Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin
- For Windows, see documentation: [Detailed instructions for Windows users](https://selenium-python.readthedocs.io/installation.html#detailed-instructions-for-windows-users)
3. Install Selenium:
- You can simply install Selenium using pip

```
pip install selenium
```

4. Alternativaly, you can install Selenium via the requirements.txt file (after cloning or downloading this repo).

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
