<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/dinis-rodrigues/gerador-horarios">
    <img src="assets/img/tsb-logo.png" alt="Logo" width="250">
  </a>

  <h3 align="center">Gerador de Horários Compactos</h3>

  <p align="center">
    A compact schedule generator for Instituto Superior Técnico courses and shifts
    <br />
    <a href="https://github.com/dinis-rodrigues/gerador-horarios" target="_blank"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://tecnicosolarboat.tecnico.ulisboa.pt/~tecnicosolarboat.daemon/horarios/#" target="_blank">View Live Application</a>
    ·
    <a href="https://github.com/dinis-rodrigues/gerador-horarios/issues" target="_blank">Report Bug</a>
    ·
    <a href="https://github.com/dinis-rodrigues/gerador-horarios/issues" target="_blank">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
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
        <li><a href="#firebase-setup">Firebase Setup</a></li>
      </ul>
    </li>
    <li><a href="#deploy">Deploy</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The great [Pedro P. Ramos](http://web.ist.utl.pt/pedropramos/horarios/) started this project idea back in 2013 releasing the first version of this compact schedule generator.

Students are allowed to quickly sort through their best possible schedule, gaining
the most of their free time in the week. It gained popularity and many used it, always with positive feedback.

Due to the lack of maintenance from the original developer, and with our own vision to improve this tool, we decided to fork the project and maintain it for the community.

### Features

- Course selection
- Shift selection
- Best outcome generation

### Built With

This is a very basic application, so no need for advanced frameworks like ReactJS,
Angular etc. Maybe in the future for extra effort points 😉
So the front-end of the application is simply developed with:

- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element)
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)
- [Javascript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)

By default, in the Sigma server cluster of Instituto Superior Técnico we have access to PHP and some
basic Python functionality. We also added a simple visit counter where the data is
stored in Firebase. Almost every task of schedule generation is performed on the
back-end with:

- [PHP](https://www.php.net)
- [Python](https://www.python.org)
- [Firebase](https://firebase.google.com)

<!-- GETTING STARTED -->

## Getting Started

This project follows a simple setup and file structure. If you would like to run this project up and running locally for yourself, follow these steps.

### Prerequisites

Clone the repository

```sh
git clone https://github.com/dinis-rodrigues/gerador-horarios.git
```

For the easy way with VS Code, install the following extensions:

- `Live Server`
- `PHP Server`

### Firebase Setup

If you would like to setup your own database for the visit counter, it only takes 2 min.

1. Create a Firebase Project [here](https://firebase.google.com)
2. Setup Realtime Database
3. Import the database template from

```sh
src/config/dbTemplate.json
```

5. Import the database rules from

```sh
src/config/dbRules.json
```

6. Go to Project Settings and get the API key, should look like this:

```js
const firebaseConfig = {
  apiKey: "AIzaSyAHPrWvVr1El3NkJd3C0gbZbiTl_weCTlE",
  authDomain: "tsb-aplication.firebaseapp.com",
  databaseURL: "https://tsb-aplication.firebaseio.com",
  projectId: "tsb-aplication",
  storageBucket: "tsb-aplication.appspot.com",
  messagingSenderId: "124968779478",
  appId: "1:124968779478:web:0a2c6266560c594a779377",
  measurementId: "G-0Z77DRSCH6",
};
```

7. Copy and replace the API configuration in

```sh
src/client/visitCount.js
```

## Deploy

If you followed all of the above steps, you can proceed to locally run the
project with VS Code by simply running the aforementioned extensions

- `Live Server`
- `PHP Server`

If you would like to deploy the application to your own server, just copy and paste all
of the files in the respective directory.

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/dinis-rodrigues/gerador-horarios/issues) for a list
of proposed features (and known issues), if any.

<!-- CONTRIBUTING -->

## Contributing

We welcome all kinds of contributions from the open-source community.

- [Contributing guidelines](assets/docs/CONTRIBUTING.md)

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

<!-- ## Contact

Dinis Rodrigues - [Linkedin](https://www.linkedin.com/in/dinis-rodrigues/) - dinis.rodrigues@tecnico.ulisboa.pt -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/dinis-rodrigues/gerador-horarios.svg?style=for-the-badge
[contributors-url]: https://github.com/dinis-rodrigues/gerador-horarios/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dinis-rodrigues/gerador-horarios.svg?style=for-the-badge
[forks-url]: https://github.com/dinis-rodrigues/gerador-horarios/network/members
[stars-shield]: https://img.shields.io/github/stars/dinis-rodrigues/gerador-horarios.svg?style=for-the-badge
[stars-url]: https://github.com/dinis-rodrigues/gerador-horarios/stargazers
[issues-shield]: https://img.shields.io/github/issues/dinis-rodrigues/gerador-horarios.svg?style=for-the-badge
[issues-url]: https://github.com/dinis-rodrigues/gerador-horarios/issues
[license-shield]: https://img.shields.io/github/license/dinis-rodrigues/gerador-horarios?style=for-the-badge
[license-url]: https://github.com/dinis-rodrigues/gerador-horarios/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dinis-rodrigues
[product-screenshot]: public/assets/images/readMeImages/appScreen.png
