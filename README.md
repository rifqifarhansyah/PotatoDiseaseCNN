# Deep Learning Project
<h2 align="center">
Potato Disease Classification Using CNN<br/>
</h2>
<hr>

## Table of Contents
1. [General Info](#general-information)
2. [Creator Info](#creator-information)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup](#setup)
6. [Usage](#usage)
7. [Video Capture](#videocapture)
8. [Screenshots](#screenshots)
9. [Structure](#structure)
10. [Project Status](#project-status)
11. [Room for Improvement](#room-for-improvement)
12. [Acknowledgements](#acknowledgements)
13. [Contact](#contact)

<a name="general-information"></a>

## General Information
A straightforward website utilizing one of the concepts of deep learning, Convolutional Neural Networks (CNN), to analyze diseases in potato plants. The program utilizes a dataset from Kaggle, specifically the [Plant Village dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village), to construct the model. The model deployed in this application achieves a confidence score exceeding 98%, with a margin of error of 1.5%. It is hoped that this application will assist farmers in identifying diseases in their potato plants early, enabling them to address the issue promptly.

<a name="creator-information"></a>

## Creator Information
| Nama                        | NIM      | E-Mail                      |
| --------------------------- | -------- | --------------------------- |
| Mohammad Rifqi Farhansyah   | 13521166 | 13521166@std.stei.itb.ac.id |

<a name="features"></a>

## Features
- Read `input` as an image
- User could `drag and drop` their picture or just `click the upload button` 

<a name="technologies-used"></a>

## Technologies Used
- FastAPI - v0.109.2
- React - v18.2.0
- Tensorflow - v2.15.0
- uvicorn - v0.27.1
- PIL - v10.2.0
- numpy - v1.26.4

> Note: The version of the libraries above is the version that we used in this project. You can use the latest version of the libraries.

<a name="setup"></a>

## Setup
1. Install all of the requirements above.
2. Clone this repository using command below:
```bash
git clone https://github.com/rifqifarhansyah/PotatoDiseaseCNN.git
```
3. Open your local directory where you cloned this repository
4. Setup the ReactJS using this command:
```bash
cd clone
npm install --from-lock-json
npm audit fix
```
5. Rename `.env.example` file with `.env`

<a name="usage"></a>

## Usage
1. To run the backend, you can use the following steps:
    - go to `api` folder
    - run this command in your terminal
    ```bash
    uvicorn main-tf-serving:app --reload --host 0.0.0.0
    ```
    - or just type
    ```bash
    python main.py
    ```
3. After that, run the frontend by following this steps:
    - go to `frontend` folder
    - run this command in your terminal
    ```bash
    npm run start
    ```
    
<a name="videocapture"></a>

## Video Capture
<nl>

![PotatoDiseaseClassification Gif](https://github.com/rifqifarhansyah/PotatoDiseaseCNN/blob/main/img/PotatoDiseaseClassification.gif?raw=true)

<a name="screenshots"></a>

## Screenshots
<p>
  <img src="/img/SS1.png/">
  <p>Figure 1. Landing Page</p>
  <nl>
  <img src="/img/SS2.png/">
  <p>Figure 2. Early Blight</p>
  <nl>
  <img src="/img/SS3.png/">
  <p>Figure 3. Healthy</p>
  <nl>
  <img src="/img/SS4.png/">
  <p>Figure 4. Late Blight</p>
  <nl>
</p>

<a name="structure"></a>

## Structure
```bash
C:.
├───.ipynb_checkpoints
├───api
├───frontend
│   ├───public
│   └───src
├───saved_model
│   └───1
│       ├───assets
│       └───variables
└───training
    ├───.ipynb_checkpoints
    ├───AugmentedImages
    ├───dataset
    │   ├───test
    │   │   ├───Potato___Early_blight
    │   │   ├───Potato___healthy
    │   │   └───Potato___Late_blight
    │   ├───train
    │   │   ├───Potato___Early_blight
    │   │   ├───Potato___healthy
    │   │   └───Potato___Late_blight
    │   └───val
    │       ├───Potato___Early_blight
    │       ├───Potato___healthy
    │       └───Potato___Late_blight
    └───PlantVillage
        ├───Potato___Early_blight
        ├───Potato___healthy
        └───Potato___Late_blight
```

<a name="project-status">

## Project Status
Project is: _complete_

<a name="room-for-improvement">

## Room for Improvement
Room for Improvement:
- Optimizing the accuracy of the model with other layering approach
- Beautify the UI of the application
- Add the mobile version

<a name="acknowledgements">

## Acknowledgements
- Thanks To Allah SWT

<a name="contact"></a>

## Contact
<h4 align="center">
  Contact Us : mrifki193@gmail.com<br/>
  2024
</h4>
<hr>