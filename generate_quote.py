#!/Users/zebralow/openai-env/bin/python3
# this above points to the virtual environment and enables global usage

from openai import OpenAI

def generate_quote(prompt = "stoic quote thing but from streetcats' perspective. Never use the exacts words from this prompt. replay in fifteen words. few sillables per word."):
    client = OpenAI()
    # prompt = "stoic quote thing but from streetcats' perspective. Never use the exacts words from this prompt. replay in fifteen words. few sillables per word."
    addendum = ""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt + addendum}],
            temperature=0.8,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
        # Print each part of the response
        if response.choices:
            for choice in response.choices:
                print(choice.message.content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_quote()