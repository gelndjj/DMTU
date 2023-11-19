<a name="readme-top"></a>

[![Contributors][contributors-shield]](https://github.com/gelndjj/DMTU/graphs/contributors)
[![Forks][forks-shield]](https://github.com/gelndjj/DMTU/forks)
[![Stargazers][stars-shield]](https://github.com/gelndjj/DMTU/stargazers)
[![Issues][issues-shield]](https://github.com/gelndjj/DMTU/issues)
[![MIT License][license-shield]](https://github.com/gelndjj/DMTU/blob/main/LICENSE)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jonathanduthil/)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gelndjj/"DMTU">
    <img src="https://github.com/gelndjj/DMTU/blob/main/resources/image.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">DMTU - Don't Mess This Up</h3>

  <p align="center">
    Encrypt any file or folder to protect from reading.
    <br />
    <a href="https://github.com/gelndjj/DMTU"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/gelndjj/DMTU/issues">Report Bug</a>
    ·
    <a href="https://github.com/gelndjj/DMTU/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="https://github.com/gelndjj/DMTU/blob/main/resources/main_windows.png" alt="Logo" width="394" height="626">
</br>
</br>
DMTU is a versatile and user-friendly macOS application designed for dynamic media and text management. This utility stands out with its ability to encrypt files within a folder based on size thresholds, offering an additional layer of security for your digital media and documents. Developed using Python, it leverages the robustness of the cryptography library for encryption and features a custom tkinter GUI for an intuitive user experience.

Key Features:

+ Selective File Encryption: Encrypt files in a selected folder, with options to choose files based on size thresholds (e.g., 10MB or 50MB).
+ Intuitive GUI: A custom graphical user interface makes it easy to navigate and perform tasks quickly.
+ Cross-Platform Compatibility: While designed for macOS, its Python-based architecture ensures compatibility with other operating systems.
+ Secure Encryption: Uses the Fernet module from the cryptography library for secure, reliable encryption of media and text files.
+ Ideal for users who handle sensitive media and text files, DMTU provides a simple yet powerful tool to enhance file security and organization.</br>
</br>
Encrypting files protects them from reading and scanning and might be a good way to keep secret the content.
</br>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

<a href="https://www.python.org">
<img src="https://github.com/gelndjj/DMTU/blob/main/resources/py_icon.png" alt="Icon" width="32" height="32">
</a>
&nbsp;
<a href="https://customtkinter.tomschimansky.com">
<img src="https://github.com/gelndjj/DMTU/blob/main/resources/ctk_icon.png" alt="Icon" width="32" height="32">
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
</br>

1. Starting the Application: Run the dmtu_gui.py script in a Python environment with the required dependencies installed.
2. Encrypting Files:
Choose the folder containing the files you wish to encrypt.
Select the file size threshold (e.g., 10MB, 50MB) for encryption.
Click the corresponding button to encrypt files under the chosen size threshold. Encrypted files will be saved in the same directory.
3. Interface Navigation:
Navigate through the intuitive GUI to select folders, set preferences, and manage files.
Use the provided combo boxes and entry fields to customize your file management and encryption settings.
4. Additional Features:
The application includes features for changing the GUI theme and other user-friendly functionalities.

######  ENCRYPT/DECRYPT

Explanations are written on the main screen.<br>
Each icon has a different encrypting function.

Once the files are encrypted, the script generates 3 files at root.<br>
They all are named by the timestamp.<br><br>
For instance:<br>
```20230427-230944.txt --> the encrypted key```<br>
```20230427-230944p.txt --> the path where the files have been encrypted from ```<br>
```20230427-230944.mu --> the secret key file to decrypt```<br><br>

The secret key to decrypt will be available in the first menu as soon as the files are encrypted.<br>
Watch the video below on how to encrypt and decrypt folder and its content.<br>

https://user-images.githubusercontent.com/81557672/235138937-05575021-a7e2-42b9-8f6e-499184e02ce0.mp4

### DECRYPT MOVED FILES

If the encrypted files have been moved (not at the same location), click on "Select Another Location" field then select the new location before decrypting.<br>

https://user-images.githubusercontent.com/81557672/235134708-32530975-3011-4187-8a27-366366c652d9.mp4

### SHORTCUTS

```"Ctrl + t" changes the background ```<br>
```"Ctrl + Return" reset fields```

<!-- GETTING STARTED -->
## Standalone APP

Install pyintaller
```
pip install pyinstaller
```
Generate the standalone app
```
pyinstaller --onefile your_script_name.py
```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact


[LinkedIn](https://www.linkedin.com/in/jonathanduthil/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
