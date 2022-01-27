![alt text for the image](images/primer.png "Primer logo")

# **Data Engineer Code Challenge**

### **Versions**
[![Generic badge](https://img.shields.io/badge/python-3.8-blue)](https://shields.io/)

### **Coverage**
[![Generic badge](https://img.shields.io/badge/linux%2FmacOS-passing-brightgreen)](https://shields.io/)

## **1. Intro**
A Data Engineer is an IT professional whose main job is to prepare data for a set of operational and analytical use cases. They are responsible for **integrating**, **consolidating**, **cleansing**, and **structuring data**.

This code challenge gathers some of the aspects mentioned above and puts the candidate through these common actions that a Data Engineer must know.

In this particular challenge, it is intended that the candidate must be responsible for developing an ETL pipeline. For that purpose, we have a JSON file with multiple data assets, with some nested fields and others that need to be transformed. Another interesting aspect of the challenge is the way that the raw data is provided: we have a unique JSON file that possesses data relative to four distinct data dimensions (`event_v2_data`, `transaction`, `transaction_request`, and `payment_instrument_token_data`). The end line of this pipeline is the loading of the data assets manipulated until then to a serverless database (i.e. SQLite).

To get to the expected outcome, the development of the solution was divided into the following modules:

# **PUT AN IMAGE HERE!**

## **2. Project Tree**
The solution presented in this repository is divided into the following modules:

1. `/configs`
Configuration files that possess data relevant to the pipeline built. We are talking about files that establish a correspondence between data types (from Python or Postgres to SQLite) and also universal variables with whom the pipeline developed governs.

2. `/data`
A folder that tries to be a local emulation of a data lake's organization. Adapted to the dimension of this challenge, this folder possesses 3 layers/zones:

>> `/raw_zone`: this zone is where the data provided to address this challenge (the JSON file that contains the 4 data assets already mentioned) is located. This data was not yet submitted to any modification or transformation, so we can look at it as being the "raw material";

>> `/curated_zone`: is the zone where the data assets will be placed after being submitted to all the required transformations. So it is clear that this zone will have 4 files corresponding to the 4 data assets that this code challenge aims for. These 4 dimensions will then be replicated on our serverless database;

>> `/consume zone`: is the dataset that is obtained after crossing the data from the 4 dimensions. It will be the data that is prepared to serve analytical use cases.

3. `docs`
Where the .md file that handles the presentation of the challenge is kept;

4. `images`
Images used on the documentation of this solution are saved in this folder;

5. `tdd_stage`
Where all the development was settled. TDD (Test Driven Development) practises were followed along the development stage, so we can look at this folder as the working area where all the methods and classes were not only developed, but tested.

## **3. TDD Pipeline**


## **4. Data Assets**


## **5. Data Lifecycle**


## **6. Production Placement**


## **7. Data Lifecycle**


## **8. Trigger the Pipeline**

