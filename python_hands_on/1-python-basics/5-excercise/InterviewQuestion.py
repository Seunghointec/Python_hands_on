# Now this is actually an interview question asked by: Google, Facebook, Amazon, Microsoft:

# DESCRIPTION:

# Given some text, our program should search for the most used character

lyrics = """
Brothers of the mine rejoice!
Swing, swing, swing with me
Raise your pick and raise your voice!
Sing, sing, sing with me
Down and down into the deep,
Who knows what we'll find beneath?
Diamonds, rubies, gold and more
Hidden in the mountain store.

Born underground, suckled from a teat of stone.
Raised in the dark, the safety of our mountain home.
Skin made of iron, steel in our bones,
To dig and dig makes us free!
Come on brothers sing with me!

I am a dwarf and I'm digging a hole
Diggy diggy hole, diggy diggy hole
I am a dwarf and I'm digging a hole
Diggy diggy hole, digging a hole!

The sunlight will not reach this low
Deep, deep in the mine
Never seen the blue moon glow
Dwarves won't fly so high
Fill a glass and down some mead!
Stuff your bellies at the feast!
Stumble home and fall asleep
Dreaming in our mountain keep

Born underground, grown inside a rocky womb
The earth is our cradle; the mountain shall become our tomb
Face us on the battlefield; you will meet your doom
We do not fear what lies beneath
We can never dig too deep

I am a dwarf and I'm digging a hole
Diggy diggy hole, diggy diggy hole
I am a dwarf and I'm digging a hole
Diggy diggy hole, digging a hole!

I am a dwarf and I'm digging a hole
Diggy diggy hole, diggy diggy hole
I am a dwarf and I'm digging a hole
Diggy diggy hole, digging a hole!

Born underground, suckled from a teat of stone
Raised in the dark, the safety of our mountain home
Skin made of iron, steel in our bones
To dig and dig makes us free
Come on brothers sing with me!

I am a dwarf and I'm digging a hole
Diggy diggy hole, diggy diggy hole
I am a dwarf and I'm digging a hole
Diggy diggy hole, digging a hole!

I am a dwarf and I'm digging a hole
Diggy diggy hole, diggy diggy hole
I am a dwarf and I'm digging a hole
Diggy diggy hole, digging a hole!
"""

# Solution:

char_freq = {}

for char in lyrics:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

char_freq_sorted = sorted(char_freq.items(), key=lambda kv: kv[1], reverse=True)

print('Most used char: ', char_freq_sorted[0])
