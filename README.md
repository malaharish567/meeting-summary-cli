## Meeting Summary CLI

A command-line tool that summarizes meeting transcripts into actionable bullet points using OpenAI’s API.

## Features
. Reads meeting transcripts from a .txt file

. Generates concise bullet-point summaries using OpenAI

. Simple and intuitive CLI interface

. Optional output file support

. Secure API key handling via environment variables

## Prompting Strategy
The summarization prompt follows the CARE framework

*Context – Defines the role and domain of the AI

*Action – Specifies what the model should do

*Result – Defines output structure and formatting

*Example – Gives an example.


## Setup Instructions

1. Create folder
   
cd meeting-summary-cli

2.Create Virtual Environment

conda create -n venv python==3.11 -y

3.Install Dependencies

pip install -r requirements.txt

4.Configure Environment Variables

OPENAI_API_KEY=your_api_key_here

5.Usage

python summarize.py sample_transcript.txt - (shows o/p in terminal)

python summarize.py sample_transcript.txt --output summary.txt   - (saves o/p to a file)
