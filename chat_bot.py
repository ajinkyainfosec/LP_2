import time

def chatbot():
    print("🤖 Hello! Welcome to ElectroBot Customer Support.")
    time.sleep(1)

    name = input("👤 May I know your name, please? ")
    print(f"\n🤖 Nice to meet you, {name}! How can I help you today?")
    time.sleep(1)

    responses = {
        "1": "Our store hours are 9 AM to 9 PM, Monday to Saturday.",
        "2": "You can track your order at: www.electrostore.com/track",
        "3": "We offer a 1-year warranty on all electronic items.",
        "4": "To return a product, visit www.electrostore.com/returns",
        "5": "We accept credit/debit cards, UPI, and net banking.",
        "6": "Yes, we do offer EMI options on select products.",
        "7": "Delivery usually takes 3–5 business days.",
        "8": "Yes, you can cancel your order before it's shipped.",
        "9": "Contact our support at support@electrostore.com or call 1800-123-456.",
        "10": "Yes, you can exchange your product within 10 days of delivery."
    }

    questions = {
        "1": "What are your store hours?",
        "2": "How can I track my order?",
        "3": "Do you offer warranty on products?",
        "4": "How do I return a product?",
        "5": "What payment methods do you accept?",
        "6": "Do you offer EMI options?",
        "7": "How long does delivery take?",
        "8": "Can I cancel my order?",
        "9": "How do I contact customer support?",
        "10": "Can I exchange a product?"
    }

    print("\nHere are some things I can help you with:\n")
    for key in questions:
        print(f"{key}. {questions[key]}")
    
    while True:
        user_input = input("\nEnter the number of your question (1–10), or type 'exit': ").strip().lower()
        if user_input == "exit":
            print(f"🤖 Thank you for chatting with us, {name}! Have a wonderful day 😊")
            break
        elif user_input in responses:
            print("🤖", responses[user_input])
        else:
            print("🤖 Sorry, I didn't understand that. Please enter a number between 1 and 10.")

# Run the chatbot
chatbot()
