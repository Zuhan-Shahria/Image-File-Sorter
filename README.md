# Image File Sorter
A python program that creates folders named after the image file types and moves each image file to its respective folder.

## How to start this program?
It's very simple just open your prefered programming software and paste the code in. After that you have to copy that path in your file explorer for which you will be sorting the images in and replace text in the code that says "PATH NAME" with your actual path.

## Can you make amendments to this program?
Yes you can. The file types I have included are JPEG, JPG, WEBP and PNG files if you have more file types, the first thing you have to do is add the name of the file type into the "folder_names" list. Secondly, you have to change the range of the FOR loop to however many elements you have in the list, e.g if you have 5 file types the range would be (0,5). Finally you want to add an ELIF statement for every new file type you have included which is done by just changing the string.
