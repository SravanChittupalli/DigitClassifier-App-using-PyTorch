# DigitClassifier-App-using-PyTorch ⑦


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
  * [Process](#process)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
* [Usage](#usage)
* [Output](#output)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)

```
├── app                                                                                 // For future implementation in 
│   ├── Models
│   │    ├── __init__.py
│   │    ├── FeedForward.py
│   │    ├── Perceptron.py
│   │    └── CNN.py
│   ├── train
│   │   ├── train_CNN.ipynb 
│   │   └── train_feedforward.ipynb
│   ├── savedModels
│   │   ├── MNIST_CNN.pth
│   │   ├── MNIST_FeedForward.pth
│   │   └── MNIST_Perceptron.pth
│   ├── utils
│   │   ├── __init__.py
│   │   └── camera.py 
│   ├── CNNClassifierApp.py
│   └── FeedforwardClassifierApp.py 
├── LICENSE                                                                             // License
├── assets                                                                              // Testing mqtt mosquitto lib
│   ├── out_vid1.mkv
│   ├── out_vid2.mkv
│   ├── output1.png 
│   ├── output2.png 
│   └── wrongop_1MNIST.png
└── README.md                                                                           // This file
```




<!-- ABOUT THE PROJECT -->
## About The Project

In this project I experimented a bit with different neural network architectures and saw how good each of the architectures were performing on MNIST dataset. 
- ### Perceptron
I tried with a perceptron first but as you know the results were not very good. The accuracy was low and even with the data from MNIST it was not giving accurate results. 
- ### FeedForward
Next I tried a feed forward neural network with one hidden layer. The results were good i.e I got an accuracy of 80% within the first few epochs. When I tested it on the MNIST test set I got around 82% accuracy which is pretty good. There is one problem. The FeedForward neural networks do not take the shape into consideration. They just see the pixel intensities at locations and produces an output. Now assume a senario where 3 was written in such a way that it is covering all the activated parts for 8, then the model can be fooled easily.
- ### CNN
That is why when I tried to input a custom image that i made with a black background gave me wierd predictions. Then I implemented a CNN architecture and still got ~83% accuracy within a few epochs. Now when I tried it on custom that I made I got good results. 


<p>
<a href="https://github.com/SRA-VJTI/practice-assignments/blob/master/Data-Relay/data-relay.md">Data Relay by SRA-VJTI</a>
</p>

This project focusses on the MQTT, Multithreading, Compression Algo and File I/O in C and C++

<!-- PROCESS -->
## Process
<br />
<p align="center">
  <img src="images/detarelayprocess.png" alt="output" width="720" height="720">
</p>
<br />

### Built With

* [Mosquitto](https://mosquitto.org/)
* [C++](https://en.wikipedia.org/wiki/C%2B%2B)
* [C](https://en.wikipedia.org/wiki/C_(programming_language))



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

* mosquitto libs for ubuntu

```sh
sudo apt search mosquitto
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
```

* Now install libmosquittopp1 for C++(optional) and libmosquitto-dev for C 

### Usage

```sh
cd src/
gcc sub_final.c -o sub_final -lmosquitto -ljson-c
gcc pub_final.c -o pub_final -lmosquitto -ljson-c -lpthread
g++ cpp_compression.cpp
```

* To run subscriber use `./sub_final` and for publisher use `./pub_final` 
Note: Run subscriber before publisher

* To compress the redundant data use `./a.out`

<!-- OUTPUT -->
## Output
<br />
<p align="center">
  <img src="images/opt.png" alt="output" width="720" height="480">
  <p align="center">
  Now it also shows compression ratio and space savings calculated according to <a href="https://en.wikipedia.org/wiki/Data_compression_ratio">Wikipedia</a>
  <br />
  <img src="images/compressionopt.png" alt="Compression Ratio" width="720" height="256">
  </p>
</p>
<br />

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/SAtacker/data-relay/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes        (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch         (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - shreyasatre16@gmail.com

Project Link: [https://github.com/SAtacker/data-relay](https://github.com/SAtacker/data-relay)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Saharsh Jain](https://github.com/saharshleo)
* [SRA-VJTI](https://github.com/SRA-VJTI)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/SAtacker/data-relay.svg?style=flat-square
[contributors-url]: https://github.com/SAtacker/data-relay/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/SAtacker/data-relay.svg?style=flat-square
[forks-url]: https://github.com/SAtacker/data-relay/network/members
[stars-shield]: https://img.shields.io/github/stars/SAtacker/data-relay.svg?style=flat-square
[stars-url]: https://github.com/SAtacker/data-relay/stargazers
[issues-shield]: https://img.shields.io/github/issues/SAtacker/data-relay.svg?style=flat-square
[issues-url]: https://github.com/SAtacker/data-relay/issues
[license-shield]: https://img.shields.io/github/license/SAtacker/data-relay.svg?style=flat-square
[license-url]: https://github.com/SAtacker/data-relay/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/atreshreyas
[product-screenshot]: images/screenshot.png
