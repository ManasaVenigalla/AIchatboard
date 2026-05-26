import os
from openai import OpenAI

key="youropenaikey"
#please fill this with your secret open ai key

messages=[]

client=OpenAI(
    api_key=key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role":"user",
            "content":message
        }
    )
    chat_completion = client.chat.completions.create( messages=messages,model="gpt-4o"
    )
    #print(chat_completion)
    message={
        "role":"assistant",
        "content":chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Maya:{message["content"]}")

if __name__=="__main__":
    print("Maya:Hi I an Maya,How may I help You\n")
    while True:
        user_question=input()
        print(f"User:{user_question}")
        completion(user_question)