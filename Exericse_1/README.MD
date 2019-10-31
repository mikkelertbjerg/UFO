# UFO Assignment 1

## Hand-in
You should hand in the material listed above, and a brief summary of which aspect of the exercise was taking you the longest time to solve, which part of the exercise was side tracking you the most (which dead-ends did you persue), and what was the most helpful information you came across (it could be someone else helping you). How can you avoid those problems in the future, and how can the helpful ressources help you in the future?

Hand-in should be done on Peergrade in self picked groups of size 1-3.

## Review:
Look at the google queries used by the group you review, and try to compare with your own. In particular, try to find cases where you and your review group was trying to find an answer to the same issue, but where you asked diffrently. Which queries leads to the best result?
Examine the pages visited by the review group. Find two sites you find trustworthy, and two which you do not find trustworty. Explain why.
Try to come up with a strategy for the review group which would have overcome their largest stumbling block.

## Question to be investigated
Steganography is the idea of hiding a message in something.

For example, to hide a message in an image, you can do the following:

The message M, is converted to a sequence of bits (often from String, to bytes, to bits).
The image is manibulated in such a manner that the least significant bit of the red values is substituted with a bit from the message.
For example, this small image contains a message:

![hidden in plain sight](https://datsoftlyngby.github.io/soft2019fall/UFO/images/Stego.png)

It is an ascii message, and the bits of the message are stored starting in pixel (0,0), next in (1,0) etc. The message is terminated with a null/0 byte.

What is the message?