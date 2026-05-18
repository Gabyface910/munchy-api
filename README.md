# Munchy API
This is the API endpoint that Munchy uses. For the app itself, see [here](https://github.com/Gabyface910/munchy).
## About the API
The Munchy API is a fork of [TheMealDB](https://themealdb.com), a crowd-sourced recipe API. For better sorting and search URLs, use TheMealDB. I just wanted to bypass Premium features so I can add stuff to the Munchy API.

SHOUTOUT: TheMealDB's premium tier is unique in that it is NOT a subscription! Check it out!
## How to use the API
Use this endpoint to find a recipe without looking for it on Munchy. Use some JS to filter it from this URL: https://raw.githubusercontent.com/Gabyface910/munchy-api/recipes.json&t={Date.now()}. `Date.now()` is what to use if it is JS, but if you are using Python, it would need `import time` and instead of `Date.now()` it would use `time.time()`
