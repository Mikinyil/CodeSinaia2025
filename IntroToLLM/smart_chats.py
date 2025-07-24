from smart_agent import SmartAgent

smart_agent = SmartAgent("llama3.2:latest")

question = input("question?> ")
while question != "/pa":
    if question != "":
        answer_text = smart_agent.chat(question)
        print(answer_text)
    question = input("question?> ").strip()
