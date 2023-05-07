## ThinkAI Morocco - 07/05/2023

ThinkAI Morocco 2023 is a 3-days AI Hackathon co-hosted by 1337AI and Math&Maroc which brings together talented teams of students from different Moroccan schools to compete in challenges that showcase their creativity and expertise. Over the course of the hackathon, participants will have the opportunity to develop new skills, collaborate with like-minded individuals, and create innovative solutions that could make a real difference in the world. Don’t miss out on this exciting opportunity to be part of the future of AI in Morocco!


## Challenge we choosed: AI Product Challenge

The goal of this challenge is to develop a product that solves a real-world problem faced by Moroccans. Participants will be required to ideate, design, and develop a working prototype of their product using AI technologies - **without any need to train the model**. The product can be in any industry, including healthcare, education, finance, and agriculture.


## Welcome to KOZINTAI - Recipe generator

**_Transform your kitchen ingredients into delicious meals with our app, powered by natural language processing technology._**

#### 1. Project Focus
KOZINTAI is a Moroccan recipe generator web app that could become a comprehensive resource for Moroccan cuisine, catering to users with different preferences and skill levels, and promoting local food culture and sustainability ^^.

This web application allows users to give ingredients they have in their kitchen to the app and get recipe suggestions based on those ingredients. The application uses natural language processing technology to generate recipe suggestions and provide step-by-step instructions on how to make the meal. This could help users make the most of the ingredients they have and reduce food waste.

- The app could suggest substitutes that would work well in the recipe (If a user is missing an ingredient or prefers a different ingredient).
- The app could allow users to specify dietary restrictions, such as gluten-free or vegan, and generate recipes that meet those requirements.
- The app could suggest recipes based on the season or time of year, featuring ingredients that are in season in Morocco.

#### 2. The architecture used
![Architecture](/docs/README.png)

Web app (React JS) **->** Call Vectors from /data to check Cosine similarity with the inputs (We used Contexte retrivel to generate vectors in /data to check cosin similiraty between 100 Marrocan recepies and the inputs from user) **->** Prompt Engineering (Generate context and guiding the model to generate useful output) **->** large language model using InstructGPT (OpenAI's GPT-3 model that is optimized to follow instructions, instead of predicting the most probable word) **->** Web app

#### 3. User Interface
![Architecture](/docs/front1.png)
![Architecture](/docs/front2.png)
![Architecture](/docs/front3.png)

#### 4. Principles used
- Prompt Engineering
- REST API
- Context retrival
- langue language model

#### 5. Requirements

#### 6. Getting started :p





