<h1 align="center">
  <br>
  <a href="https://www.marvelsnap.com"><img src="https://user-images.githubusercontent.com/25803231/210183311-556aafb7-1690-4a17-a958-9c622d8f6f07.png" alt="Markdownify" width="200"></a>
  <br>
  Marvel Snap Bot
  <br>
</h1>

<h4 align="center">A computer vision bot made with <a href="https://opencv.org/" target="_blank">OpenCV</a> and <a href="https://developer.android.com/studio/command-line/adb" target="_blank">ADB</a>.</h4>

<p align="center">
  <a href="https://badge.fury.io/js/electron-markdownify">
    <img src="https://badge.fury.io/js/electron-markdownify.svg"
         alt="Gitter">
  </a>
  <a href="https://gitter.im/amitmerchant1990/electron-markdownify"><img src="https://badges.gitter.im/amitmerchant1990/electron-markdownify.svg"></a>
  <a href="https://saythanks.io/to/bullredeyes@gmail.com">
      <img src="https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg">
  </a>
  <a href="https://www.paypal.me/AmitMerchant">
    <img src="https://img.shields.io/badge/$-donate-ff69b4.svg?maxAge=2592000&amp;style=flat">
  </a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#improvements">Improvements</a>
</p>

![screenshot](https://raw.githubusercontent.com/amitmerchant1990/electron-markdownify/master/app/img/markdownify.gif)
![Capture](https://user-images.githubusercontent.com/25803231/210183326-e543da5a-ef14-44e5-8cd5-770eec453c02.PNG)

## Key Features

- Card detection
  - Detect player cards on live time
- Automate the decision making
- Mana consumption tracked
- Fields with different priorities and constraints
- ADB Support (Bluestacks, any version)
- Global utils to apply for other computer vision bots
- Calculate the power of the cards
- Farm missions
- Farm season pass
- Play kazoo decks with applied logic
- Quick usage

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com), [OpenCV](https://opencv.org/), [Bluestacks](https://www.bluestacks.com/es/index.html) and [Python 3](https://www.python.org/).
From your command line:

```bash
# Clone this repository
$ git clone https://github.com/AdriaGual/marvel-snap-bot

# Go into the repository
$ cd marvel-snap-bot

# Install dependencies
$ pip install -r requirements.txt

# Run the bot
$ python start.py
```

> **Note**
> In order to see the bot start, you must install the game (Marvel Snap Bot) on Bluestacks and start it.

## Improvement

There are plenty of improvements still, here's a bunch of:

- Fields should be detected automatically
- The points of each field is not tracked, it can be done with pytesseract
- The cards on the player field don't show the power
- Detect the enemy cards on the field

## License

MIT

---
