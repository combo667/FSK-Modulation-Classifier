# Drone Signal Classification Using VGG16

## Description
In this project, I developed a binary classification model to distinguish Frequency Shift Keying (FSK) signals from non-FSK signals, such as Quadrature Amplitude Modulation (QAM), Phase Shift Keying (PSK), and Amplitude Shift Keying (ASK). The classification task leverages **Constellation Diagrams** as input features, which visually represent the phase and amplitude characteristics of the modulated signals. 

For signal classification, I employed the **VGG16** deep learning architecture, known for its effectiveness in image recognition tasks. The model is trained to accurately identify distinguishing features between FSK and non-FSK signals, utilizing the depth of VGG16's convolutional layers to extract and analyze complex signal patterns from the constellation diagrams.

This repository contains all the necessary files for generating constellation diagrams, model training, and datasets.

## Data Used
1. **RFD900 Telemetry IQ Frames.**
2. **Signals captured using a Vector Signal Generator (VSG)** of different modulation types using Pluto SDR.

## Dataset
The dataset contains two folders:
- `FSK`: Contains 8000 constellation images of size 224x224 representing FSK signals.
- `NOT_FSK`: Contains 8000 constellation images of size 224x224 representing non-FSK signals (e.g., QAM, PSK, ASK).

## Outcomes
The `Outcomes` folder contains the following files:
1. **Confusion_Matrix**: The confusion matrix obtained by testing the model.
2. **AUC_Plot_Of_Model**: The Area Under Curve (AUC) plot of the model.
3. **Training_Progress**: Logs showing the model's training progress.
4. **TestAccuracy**: Test accuracy results of the model on the test dataset.

## Report
The `Report` folder contains the complete report of this project.

## Scripts
1. **plotConstellationBins_of_IQ_CSV_Files.py**: This script generates constellation diagrams from a CSV file of IQ values (telemetry data from RFD900).
2. **plotConstellationBins_of_VSG_Data.py**: This script generates constellation diagrams from `.complex16s` files captured using a Vector Signal Generator (VSG).
3. **NewScript_FSK_NOTFSK_Modulation_Classification_NEW.ipynb**: This is the main script defining the VGG16 model and including code for testing.

## Model
The `Model` folder contains the trained model file:
- **vgg16_FSK_NOTFSK.h5**: The trained VGG16 model for classifying FSK and non-FSK signals. This can be loaded with the `load_model` function for further testing or inference.

## Captured Signals
The `CapturedSignalsFromVsgForModulationClassification` folder contains `.complex16s` signal files captured using the VSG for different modulation types. These signals were used to generate the constellation diagrams for training and testing.

**Details of Captured Signals:**
- Samples Captured: 15M
- Sampling Rate: 2 MHz
- Frequency: 1 GHz

## Dataset Location : [Click Here]([URL](https://drive.google.com/drive/folders/18eN73YtTSq2oIr6DMJ8n8drYpesFLfij?usp=sharing))
1. `rfd900_fsk_csv_files.zip`: This file contains telemetry data of RFD900, which includes 2 FSK signals used for plotting constellation diagrams and model training.
2. `CapturedSignalsFromVsgForModulationClassification`: This folder contains the VSG-captured signal data used for generating constellation diagrams using Adalm Pluto.

---


