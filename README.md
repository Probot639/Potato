# Potato
This is a text game heavily based on the game Potato by Oliver Darkshire. I say "based on" because I added some things to the game to make it winnable. I also added the Wizard Council, but that's unimportant. 

## Differences between this game and the main game at [Oliver Darkshire's Patreon](https://www.patreon.com/deathbybadger).
* Some of the text is different, as I wanted the player to know the general idea of how the different events affect their resources
* There are different modes, from Easy to "Let the Wizarding Council choose for you". This is because the game by itself is very hard, and not very winnable. But to keep true to the source material, the [HARD] mode is what Oliver Darkshire made.
* To make the game work, I had to make another hidden counter called `potato_v_orc`, in my wonderful variable naming conventions. This is hidden, but it counts how many potatoes you need to be able to remove an orc, and if you have too little potatoes, it doesn't give you this option. 
* I hope python's `random` library is indeed random, since thats what's doint the dice rolls. Fun!
* The wait time between text sections may be a bit too long, I set it to 2.5 by default, but I may change it depending on how the Wizard Council feels
* The Wizard Council wishes you a good day

##### i love finding issues with my game while i'm writing the readme


## TODOs
* Going to change wieghts until it works
* Going to add a function where you can always *try* to remove an orc using a potato, and the difficulty gets easier as you use more potatoes until it passes the `potato_v_orc` value at which it's an auto success, since getting locked in an unwinnable state is still too easy.
