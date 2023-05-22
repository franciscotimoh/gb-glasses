<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<h3 align="center">Guidance Glasses</h3>

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
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a continuation of a senior design project titled, "Guidance Glasses", which used YoloV5 Image Recognition to create a model that can distinguish between walk and wait signs at crosswalks. 

The goal of continuing this project was to increase the reliability of the model as well as add extra sensors to assist in making the decision to cross as well as with obstacles during crossing.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
Python 3.8.10 (YoloV5, PyTorch, PyAudio)

C++ (MaxSonar-EZ0 Sensor https://github.com/gauravk5/MaxSonar-EZ0-Sensor)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

Here is a guide on how to install and set up everything required to run this project. Ensure that each download is working according to each step before proceeding to the next.

### Prerequisites

1. Install YoloV5
You may download directly as a Zip file from https://github.com/ultralytics/yolov5
You may also use `git clone` to clone the repository
  WARNING: Make sure to use the SSH key. We ran into a lot of environmental setup issues with HTTPS setup.
3. Install Python 3.8 or higher and set to PATH.
4. Install CUDA, selecting the options that apply to your machine.
5. Install PyTorch, again, selecting the options that apply to your machine.
6. In the YoloV5 file, open Terminal (or your OS's equivalent) and run `pip install -r requirements.txt` to download all necessary modules and components. 
7. Ensure that YoloV5 works by running this code in the Terminal of your YoloV5 directory: `python detect.py --source 0`
Make sure you have a webcam or camera plugged in into your work station.

### Installation

Clone the repository using git to download the project's files.
   ```sh
   git clone https://github.com/timbim1681/gb-glasses
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

Once you have installed the necessary prerequisites and cloned the repository, you can run the main function to test its functionality.

If you wish to run the indivdual pieces (camera, microphone, ultrasonic), they are able to be run standalone by their functions.

<!-- USAGE EXAMPLES -->
## Usage

First iteration example: https://youtu.be/HQ8TKWEDKyo

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Complete individual microphone and ultrasonic code
- [ ] Integrate each piece into the main function
- [ ] Improve the training for the image recognition model, add arbitrary weights for other pieces, further integrate main function
    - [ ] Haptic feedback for walking with ultrasonic code

### Future Features
1. Use a GRU to create a model for the integration of camera, microphone, and ultrasonic input to provide a walk or wait output based on real-life training

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

As this is a closed team project, we will not be taking any direct pull requests or contributions. For any potential comments or concerns, contact one of the contributors to the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Tim Oh - FranciscoTimOh@gmail.com

Donovan Chen - DonovanAChen@gmail.com

Jake Silverman - jlsilverman54@gmail.com

Diego Solorzano - diegoasolo12@gmail.com

Luke Vargas - lukevargas34@gmail.com

Hyungcheol Kim - hckimhyungcheol@gmail.com

Project Link: [https://github.com/timbim1681/gb-glasses](https://github.com/timbim1681/gb-glasses)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Special thanks to Jeffrey Truong and his team members Claire Hyon, Joshua Liu, and Brandon Takaki, as well as Professor Marco Levorato for permission and guidance regarding building upon their initial project
* Roboflow Universe (https://universe.roboflow.com/) for access to public, labelled datasets
* @guaravk5 for the MaxSonar-EZ0-Sensor repository used in integration of ultrasonic sensor and haptic feedback

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
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
