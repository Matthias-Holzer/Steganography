# Steganography
The art of hiding information in plain sight.

## Showcase
You never know what you don't see. This is just a normal image, right? Well, what if I told you that I manage to hide the entire Bee Movie Script in it?

![image](out.png)
![image1](doc/img1.png)

## How it works
You will not find it by zooming in or staring long enough at it. To find the information I have to tell you where I hid it. 

Every image consists of pixels
![pixels](doc/img2.png)

Every pixel consists of a red a green and a blue value (RGB)

![pixel](doc/img3.png)

Every value consists of 8 bits

![bits](doc/img4.png)

I use the last two bits to store the hidden information. Therefore the values change just a tiny bit. So it is unnoticeable to the human eye. 

# Comparison
## Original Image
![ogi](img.jpg)
## Image with hidden information
![bee](out.png)