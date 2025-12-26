import os
from dotenv import load_dotenv
import argparse
from openai import OpenAI 
import sys 

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def read_transcript(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Transcript file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        raise ValueError("Transcript file is empty")

    return content 

def generate_summary(transcript: str) -> str:
    client = OpenAI()

    prompt = f"""
CONTEXT:
You are an AI assistant designed to summarize meeting transcripts for engineering and product teams.

ACTION:
Read the meeting transcript carefully and identify the most important information discussed.

RESULT:
Generate a concise bullet-point summary that includes:
- Key discussion points
- Decisions made
- Action items or next steps

Formatting rules:
- Use bullet points only
- Keep each bullet short and clear
- Do not add explanations or extra text

EXAMPLE:
Input Transcript:
"Alice: We need to improve API performance.
Bob: Latency is high due to database queries.
Alice: Let's add caching and create Jira tickets."

Output Summary:
• Discussed API performance issues
• Identified database queries as a latency cause
• Decided to implement caching
• Jira tickets to be created for optimization

MEETING TRANSCRIPT:
\"\"\"
{transcript}
\"\"\"
"""


    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip() 

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="CLI tool to summarize meeting transcripts using OpenAI"
    )
    parser.add_argument("transcript", help="Path to meeting transcript (.txt)")
    parser.add_argument(
        "-o",
        "--output",
        help="Optional output file to save the summary",
    )

    args = parser.parse_args()

    try:
        transcript = read_transcript(args.transcript)
        summary = generate_summary(transcript)

        print("\nMeeting Summary:\n")
        print(summary)

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(summary)
            print(f"\nSummary saved to {args.output}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()