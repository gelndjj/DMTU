# DMTU - Don't  Mess This Up
_DMTU is a file encryption tool written in Python._

	\|/          (__)    
	     `\------(oo)
	       ||    (__)
	       ||w--||     \|/
	   \|/

### SUMMARY
*_DMTU Encrypt/Decrypt any files using the Fernet module._*
### SCREENSHOTS

![Screenshot](https://github.com/gelndjj/DMTU/blob/main/screenshots/main_600x900.png)

### HOW IT WORKS - VIDEOS
######  ENCRYPT/DECRYPT

Explanations are written on the main screen.<br>
Each icons has a different function to encrypt/decrypt.

Once the files are encrypted, the script generates 3 files at root.<br>
They all are named by the timestamp.<br><br>
For instance:<br>
```20230427-230944.txt --> the encrypted key```<br>
```20230427-230944p.txt --> the path where the files have been encrypted from ```<br>
```20230427-230944.mu --> the necessary secret key file to decrypt```<br><br>

The necessary secret key to decrypt will be available in the first menu as soon as the files are encrypted.<br>
Watch the video below on how to encrypt and decrypt folder and its content.<br>

https://user-images.githubusercontent.com/81557672/235138937-05575021-a7e2-42b9-8f6e-499184e02ce0.mp4

### DECRYPT MOVED FILES

If the encrypted files have been moved (not at the same location), click on "Select Another Location" field and select the new location before decrypting.<br>

https://user-images.githubusercontent.com/81557672/235134708-32530975-3011-4187-8a27-366366c652d9.mp4

### SHORTCUTS

```"Ctrl + t" changes the background ```<br>
```"Ctrl + Return" reset fields```

### REQUIREMENTS INSTALLATION
```
pip install -r requirements.txt
```
### CLONE REPO
```
git clone https://github.com/gelndjj/DMTU.git
```
