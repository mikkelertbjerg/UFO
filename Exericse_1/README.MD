# UFO Assignment 1

Question to be investigated
Steganography is the idea of hiding a message in something.

For example, to hide a message in an image, you can do the following:

The message M, is converted to a sequence of bits (often from String, to bytes, to bits).
The image is manibulated in such a manner that the least significant bit of the red values is substituted with a bit from the message.
For example, this small image contains a message:

![hidden in plain sight](https://datsoftlyngby.github.io/soft2019fall/UFO/images/Stego.png)

It is an ascii message, and the bits of the message are stored starting in pixel (0,0), next in (1,0) etc. The message is terminated with a null/0 byte.

What is the message?