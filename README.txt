Test application to determine whether the approach from https://stackoverflow.com/q/3646036/1709587 works.

Usage instructions:

* Install Python
* Install Flask (e.g. `sudo pip install Flask`)
* Run `app.py` (e.g. `sudo python app.py`)
* Open the browser you want to test
* Go to http://localhost/static/preload.html
* Wait for 30 seconds
* Go to http://localhost/static/kittens.html

If the first 11 kittens load instantly, the `preloadImage` function works in that browser. If they load after 10 seconds, it does not work. (The final kitten is a control kitten and should always take 10 seconds to load.)

See https://stackoverflow.com/a/56012084/1709587 for explanation.
