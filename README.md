# Text-Summarizer-Project In Progress

## Description
The Text-Summarizer-Project is an advanced natural language processing (NLP) application that aims to automatically generate concise summaries of large blocks of text. With the ever-increasing amount of information available online and in various documents, extracting key information efficiently has become a crucial task. This project addresses the need for effective and accurate text summarization by utilizing cutting-edge NLP techniques.

The primary objective of the Text-Summarizer-Project is to develop a robust and versatile system capable of summarizing a wide range of textual data, including articles, research papers, news reports, and other lengthy documents. The system will employ state-of-the-art algorithms and models to analyze the input text, identify important sentences, and generate concise summaries that capture the essence of the original content.

## Website Link
https://

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

## Results

## Contributions
Contributions to this project are welcome! To contribute, please follow the standard GitHub workflow for pull requests.

## Contact Information
If you have any questions or comments about this project, feel free to contact the project maintainer at prajwalgbdr03@gmail.com.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Run the project locally
Clone the project -
```bash
git clone https://github.com/praj2408/Text-Summarizer-Project
```
Install the requirements - 
```bash
pip install -r requirements.txt
```
- python app.py Enjoy the project in a local host
