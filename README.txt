Test application to determine whether the approach from https://stackoverflow.com/q/3646036/1709587 works.

Usage instructions:

* Install Python
* Install Flask (e.g. `sudo pip install Flask`)
* Run `app.py` (e.g. `sudo python app.py`)
* Open the browser you want to test
* Go to http://localhost/static/preload.html
* Wait for a minute
* Go to http://localhost/static/kittens.html

If the first 23 kittens load instantly, the `preloadImage` function works in that browser. If they load after 10 seconds, it does not work. (The final kitten is a control kitten and should always take 10 seconds to load.)

When visiting http://localhost/static/preload.html, you may also want to look at either your browser's dev tools or the request log that Flask automatically prints to your terminal. You should see requests being responded to in batches 10 seconds apart. This is because there is a limit to how many requests the browser is willing to send simultaneously. If, despite this, the first 23 kittens on kittens.html load instantly, you can infer that this maximum number of parallel requests does not act as a limit on the number of images that can be preloaded in this way.

See https://stackoverflow.com/a/56012084/1709587 for explanation.
