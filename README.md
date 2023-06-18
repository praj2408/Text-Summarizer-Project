# Text-Summarizer-Project

## Description
The Text-Summarizer-Project is an advanced natural language processing (NLP) application that aims to automatically generate concise summaries of large blocks of text. With the ever-increasing amount of information available online and in various documents, extracting key information efficiently has become a crucial task. This project addresses the need for effective and accurate text summarization by utilizing cutting-edge NLP techniques.

The primary objective of the Text-Summarizer-Project is to develop a robust and versatile system capable of summarizing a wide range of textual data, including articles, research papers, news reports, and other lengthy documents. The system will employ state-of-the-art algorithms and models to analyze the input text, identify important sentences, and generate concise summaries that capture the essence of the original content.

## Website
![](https://github.com/praj2408/Text-Summarizer-Project/blob/main/images/website.jpg)

### Key Features and Functionality:

1. Text Preprocessing: The system will preprocess the input text by removing noise, punctuation, and stopwords to enhance the quality of the summaries generated.
2. Sentence Extraction: Advanced NLP techniques will be employed to identify key sentences from the input text that best represent the main ideas and concepts.
3. Semantic Understanding: The system will leverage semantic analysis to comprehend the meaning of the text and identify relevant information to include in the summary.
4. Summarization Techniques: The project will explore various approaches to summarization, including extractive and abstractive methods. Extractive summarization will involve selecting and combining important sentences, while abstractive summarization will generate summaries by paraphrasing and restructuring the text.
5. Length Control: The system will provide options to adjust the length of the generated summaries, allowing users to obtain both short and comprehensive summaries based on their preferences.
6. User Interface: A user-friendly interface will be developed to facilitate easy input of text and display the generated summaries. The interface may include additional features such as text highlighting and source citation.
### Benefits and Impact:
The Text-Summarizer-Project offers several benefits and potential applications, including:

- Time-saving: Users can quickly obtain condensed summaries of lengthy texts, enabling them to digest information more efficiently.
- Research and Knowledge Management: Researchers, students, and professionals can leverage the system to extract key insights from large volumes of academic papers, reports, and other research materials.
- Content Curation: Journalists, content creators, and publishers can utilize the system to generate succinct summaries of news articles, blog posts, and online content, aiding in content curation and enhancing reader engagement.
- Language Learning: Language learners can use the summarizer to practice comprehension skills and extract key information from foreign language texts.
- Information Retrieval: Search engines and information retrieval systems can integrate the summarizer to provide concise summaries alongside search results, enhancing user experience.

The Text-Summarizer-Project aims to revolutionize the way we consume and process information, empowering users with efficient and accurate text summarization capabilities.

## Dataset 
Samsum dataset - https://huggingface.co/datasets/samsum

### Dataset Summary
The SAMSum dataset contains about 16k messenger-like conversations with summaries. Conversations were created and written down by linguists fluent in English. Linguists were asked to create conversations similar to those they write on a daily basis, reflecting the proportion of topics of their real-life messenger convesations. The style and register are diversified - conversations could be informal, semi-formal or formal, they may contain slang words, emoticons and typos. Then, the conversations were annotated with summaries. It was assumed that summaries should be a concise brief of what people talked about in the conversation in third person. The SAMSum dataset was prepared by Samsung R&D Institute Poland and is distributed for research purposes (non-commercial licence: CC BY-NC-ND 4.0).

### Data Instances
The created dataset is made of 16369 conversations distributed uniformly into 4 groups based on the number of utterances in con- versations: 3-6, 7-12, 13-18 and 19-30. Each utterance contains the name of the speaker. Most conversations consist of dialogues between two interlocutors (about 75% of all conversations), the rest is between three or more people

The first instance in the training set: {'id': '13818513', 'summary': 'Amanda baked cookies and will bring Jerry some tomorrow.', 'dialogue': "Amanda: I baked cookies. Do you want some?\r\nJerry: Sure!\r\nAmanda: I'll bring you tomorrow :-)"}

### Data Fields
- dialogue: text of dialogue.
- summary: human written summary of the dialogue.
- id: unique id of an example.

### Data Splits
- train: 14732
- val: 818
- test: 819


## Model Information
PEGASUS is a state-of-the-art model for abstractive text summarization, developed by Google AI. It is a transformer-based model that is trained on a massive dataset of text and code. PEGASUS can generate summaries that are both informative and fluent, and it has been shown to outperform other models on a variety of summarization tasks.

PEGASUS is trained using a technique called masked language modeling. In masked language modeling, the model is given a sequence of text with some of the words masked out. The model then learns to predict the missing words. This helps the model to learn the relationships between words and phrases, and it also helps the model to learn how to generate text that is fluent and grammatically correct.

PEGASUS is a powerful tool for abstractive text summarization. It can be used to generate summaries of news articles, research papers, and other long documents. PEGASUS can also be used to generate summaries of code, which can be helpful for developers who need to understand the code of a large project.

Here are some of the key features of PEGASUS:

- It is a transformer-based model, which is a type of neural network that has been shown to be effective for a variety of natural language processing tasks.
- It is trained on a massive dataset of text and code, which gives it a strong understanding of the relationships between words and phrases.
- It can generate summaries that are both informative and fluent.
- It has been shown to outperform other models on a variety of summarization tasks.

PEGASUS is a promising new model for abstractive text summarization. It has the potential to revolutionize the way that we summarize text, and it could be used in a variety of applications, such as news aggregation, research paper summarization, and code summarization.

## Results
We conducted one epoch of training due to low computing power on our model, but unfortunately, the achieved accuracy was relatively low. The model's performance during this initial training phase did not meet our expectations. We acknowledge that further iterations and adjustments are necessary to improve accuracy and enhance the model's capabilities. The low accuracy obtained after one epoch suggests that additional training or modifications to the model architecture, hyperparameters, or dataset may be required to achieve desired performance levels. Further investigation and experimentation will be conducted to address these concerns and enhance the accuracy of the model.

## Contributions
Contributions to this project are welcome! To contribute, please follow the standard GitHub workflow for pull requests.

## Contact Information
If you have any questions or comments about this project, feel free to contact the project maintainer at prajwalgbdr03@gmail.com.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## How to run the project?

### STEPS:

Clone the repository

```bash
git clone https://github.com/praj2408/Text-Summarizer-Project
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python==3.8 -y
```

```bash
conda activate summary
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Prajwal Krishna
Data Scientist
Email: prajwalgbdr03@gmail.com

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 635735097495.dkr.ecr.us-east-1.amazonaws.com/text-s

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  635735097495.dkr.ecr.us-east-1.amazonaws.com/text-s

    ECR_REPOSITORY_NAME = simple-app
