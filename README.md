# Munchy API
This is the API endpoint that Munchy uses. For the app itself, see [here](https://github.com/Gabyface910/munchy).
## How to use the API
Use this endpoint to find a recipe without looking for it on Munchy. Use some JS to filter it from this URL: https://raw.githubusercontent.com/Gabyface910/munchy-api/recipes.json&t={Date.now()}. `Date.now()` is what to use if it is JS, but if you are using Python, it would need `import time` and instead of `Date.now()` it would use `time.time()`
