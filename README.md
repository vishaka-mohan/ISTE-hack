# DeepStudy

### Inspiration  
Have you ever gone through the pain of having to read piles of course materials, research papers and articles before a test but didn't really have enough time to do so? As students, we all must have experienced this. There is just so much content to understand and grasp that we often miss out on a few important points. Moreover, skimming through the text alone will not help us in extracting important information from it - and of course, making notes is such a drag. 
<br>
We therefore decided to come up with <strong>DeepStudy</strong> - a web application for students to help them grasp all the critical information from the material they're reading by generating a summary, highlighting important keywords and scientific formulae and producing a list of short questions with answers to maximize the information retention and also to save time. 

### What it does 

DeepStudy allows you to enter the text for which you'd like to make notes. It runs the NLP algorithms and then generates the following information extracted from the text that you entered:
1. Summary - A brief summary of the passage is generated which you can go through without having to read the original text entirely. 
2. Keywords - A list of important keywords is produced from the passage so that you can pay more attention to these terms.
3. Scientific formulae - It also produces a list of important scientific formulae found in the text entered.
4. Chemical terminology - You get all the chemistry-related terms extracted from the passage which allows you to memorize the formulae.
5. Question and Answers - This is the most important feature of the website. It generates a list of short questions with answers for the students to maximize the information retention and to test themselves.

You can also choose to upload an image of the passage and you'd get all the results listed above. It provides a download pdf option to save all these results for later use.

### How we built it
This website has been built using HTML, CSS and Javascript for the Frontend and Flask backend. All the NLP models were built using tensorflow, nltk, spacy. 
### Challenges that we ran into:
We experienced some issues in training the models (quite slow) and integrating it on flask since this is the first time we're using flask
### Achievements that we are proud of: 
 The fact that we were able to put together these NLP models and build a flask app which is something new for us in such a short period of time.
### Future scope: 
We hope to improve the performance of the summarization and the question-answer generation models so that it is applicable in all contexts. We'll also deploy the app in future since we couldn't do it now.

### How to run it
- [x] Clone the repository to your local directory
 - `git clone https://github.com/vishaka-mohan/ISTE-hack.git`
 
- [x] Activate your virtual environment. Follow steps in this link to create your virtual environment : <a href=https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/>Click here</a>

- `pip install virtualenv`
 - `virtualenv env`
 - `env\Scripts\activate`

- [x] Install packages from req.txt
- ` pip install -r req.txt `

- [x] Run app.py file 
- ` python app.py `


Now you can see our app running on 127.0.0.1:5000! Register with an account and try it out for yourself.
 

 


### Built With 
-	Python
-	Flask
-   spacy
-   tensorflow
-   nltk
-	Javascript
-	HTML
-	CSS

### Website screenshots
<br>
Landing page
<p  align="center"><img height= "600" width = "700" src = "https://github.com/abhishek0405/DeepStudy/blob/main/Screenshots/Home.PNG"></p>
<br>
Login page
<p  align="center"><img height= "600" width = "700" src = "https://github.com/abhishek0405/DeepStudy/blob/main/Screenshots/Login.PNG"></p>
<br>
Input text or upload image
<p  align="center"><img height= "600" width = "700" src = "https://github.com/abhishek0405/DeepStudy/blob/main/Screenshots/Upload%20Form.PNG"></p>
<br>
Quick summary
<p  align="center"><img height= "600" width = "700" src = "https://github.com/abhishek0405/DeepStudy/blob/main/Screenshots/Summary_Output.PNG"></p>
<br>
Smart practice
<p  align="center"><img height= "600" width = "700" src = "https://github.com/abhishek0405/DeepStudy/blob/main/Screenshots/Summary_Output.PNG"></p>
<br>
Pdf download
<p  align="center"><img height= "600" width = "400" src = "https://github.com/abhishek0405/DeepStudy/blob/main/Screenshots/pdf_output.PNG"></p>
<br>


### Team 
- [Abhishek Anantharam](https://github.com/abhishek0405) 
- [Vishaka Mohan](https://github.com/vishaka-mohan)


