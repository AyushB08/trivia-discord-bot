from typing import Final
import os
import random
from dotenv import load_dotenv
from discord import Intents, Client, Message

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

#GENERATED USING GEMINI
trivia_questions = [
    "What is the capital of France?",
    "Which planet is known as the Red Planet?",
    "What is the tallest mountain in the world?",
    "What is the largest ocean on Earth?",
    "What is the name of the world's most famous painting by Leonardo da Vinci?",
    "What is the chemical symbol for gold?",
    "How many hearts does an octopus have?",
    "What year did World War II begin?",
    "What is the capital of Australia?",
    "Which country is home to the Great Wall of China?",
    "What is the smallest country in the world by land area?",
    "What is the name of the fictional detective created by Arthur Conan Doyle?",
    "What is the currency of Japan?",
    "What is the largest bone in the human body?",
    "Which sea separates Europe and Africa?",
    "What is the national bird of the United States?",
    "What is the name of the largest desert in the world?",
    "What is the capital of Germany?",
    "What is the most abundant element in the Earth's atmosphere?",
    "What is the Pythagorean Theorem?",
    "In which city are the Olympic rings permanently displayed?",
    "What is the nickname for New York City?",
    "What is the first book of the New Testament in the Bible?",
    "What is the largest freshwater lake by volume?",
    "What is the capital of Canada?",
    "What is the tallest building in the world?",
    "What is the largest living organism on Earth?",
    "What is the name of the world's largest ocean liner?",
    "What is the capital of Scotland?",
    "What is the name of the world's first commercially successful smartphone?",
    "What is the largest living land animal?",
    "What is the name of the world's most famous children's book character created by A.A. Milne?",
    "What is the national sport of Canada?",
    "What is the name of the world's most famous active volcano located in Hawaii?",
    "In which year was the internet invented?",
    "What is the largest hot desert in the world?",
    "What is the name of the world's first artificial heart valve recipient?",
    "What is the capital of New Zealand?",
    "What is the name of the largest canyon in the world by volume?"
]

trivia_solutions = [
    ["Madrid", "London", "Berlin", "Paris"],
    ["Venus", "Jupiter", "Mars", "Saturn"],
    ["K2", "Mount Everest", "Kangchenjunga", "Lhotse"],
    ["Atlantic", "Pacific", "Indian", "Arctic"],
    ["The Creation of Adam", "The Last Supper", "Mona Lisa", "The Virgin of the Rocks"],
    ["Ag", "Au", "Cu", "Fe"],
    ["One", "Two", "Three", "Eight"],
    ["1939", "1941", "1943", "1945"],
    ["Sydney", "Melbourne", "Canberra", "Perth"],
    ["Japan", "Korea", "China", "India"],
    ["Vatican City", "Monaco", "Nauru", "Tuvalu"],
    ["Sherlock Holmes", "Hercule Poirot", "Miss Marple", "Adrian Monk"],
    ["Yen", "Yuan", "Won", "Rupee"],
    ["Femur", "Tibia", "Fibula", "Clavicle"],
    ["Mediterranean Sea", "Red Sea", "Black Sea", "Caspian Sea"],
    ["Bald Eagle", "Golden Eagle", "Hawk", "Falcon"],
    ["Sahara Desert", "Gobi Desert", "Australian Outback", "Kalahari Desert"],
    ["Berlin", "Munich", "Hamburg", "Cologne"],
    ["Nitrogen", "Oxygen", "Argon", "Carbon Dioxide"],
    ["a^2 + b^2 = c^2", "a + b = c", "a x b = c", "a / b = c"],
    ["Athens", "London", "Rio de Janeiro", "Beijing"],
    ["The Big Apple", "The Windy City", "The City of Angels", "The Emerald City"],
    ["Matthew", "Mark", "Luke", "John"],
    ["Caspian Sea", "Lake Superior", "Lake Victoria", "Lake Baikal"],
    ["Ottawa", "Toronto", "Montreal", "Vancouver"],
    ["Burj Khalifa", "Shanghai Tower", "Abraj Al-Bait Clock Tower", "One World Trade Center"],
    ["Giant Sequoia", "Honey Fungus", "Aspen Tree", "Bristlecone Pine"],
    ["Queen Mary 2", "Oasis of the Seas", "Harmony of the Seas", "Wonder of the Seas"],
    ["Edinburgh", "Glasgow", "Aberdeen", "Dundee"],
    ["Blackberry", "iPhone", "Motorola RAZR", "Nokia 3310"],
    ["Elephant", "Giraffe", "Hippopotamus", "Rhinoceros"],
    ["Winnie the Pooh", "Harry Potter", "Peter Pan", "Alice"],
    ["Ice Hockey", "Basketball", "Soccer", "Cricket"],
    ["Mount Fuji", "Mount Kilimanjaro", "Mount Vesuvius", "Kilauea"],
    ["1950", "1960", "1970", "1980"],
    ["Barney Clark", "Christiaan Barnard", "Willem Kolff", "Walton Lillehei"],
    ["Sydney", "Melbourne", "Wellington", "Auckland"],
    ["Grand Canyon", "Yarlung Tsangpo Canyon", "Colca Canyon", "Fish River Canyon"],
]

correct_answers = [
    4,
    3,
    2,
    2,
    3,
    2,
    3,
    1,
    3,
    3,
    1,
    1,
    2,
    4,
    1,
    2,
    1,
    1,
    2,
    1,
    1,
    1,
    3,
    4,
    3,
    1,
    1,
    4,
    3,
    2,
    1,
    1,
    1,
    4,
    3,
    1,
    1,
    3,
    1
]


in_trivia = False
curr_index = 0

async def send_trivia_question(message: Message) -> None:
    global curr_index, in_trivia

    curr_index = random.randint(0, len(trivia_questions) - 1)
    question = trivia_questions[curr_index]
    solutions = trivia_solutions[curr_index]

    trivia_message = "**Trivia Question:**\n" + question + "\n\n**Possible Solutions:**\n"
    for i in range(len(solutions)):
        trivia_message += str(i + 1) + ". " +  str(solutions[i]) + "\n"

    trivia_message += "\nType the number corresponding to the correct solution."
    await message.channel.send(trivia_message)

@client.event
async def on_ready() -> None:
    print(str(client.user) + " is now running!")

@client.event
@client.event
async def on_message(message: Message) -> None:
    global in_trivia, curr_index

    if message.author == client.user:
        return

    input_content = message.content.lower()

    if in_trivia:
        if (input_content == "stop"):
            await message.channel.send("Thanks for playing! Type '**trivia**' to start again.")
            in_trivia = False

        elif input_content.isdigit():
            selected_option = int(input_content)
            if 1 <= selected_option <= len(trivia_solutions[curr_index]):
                if selected_option == correct_answers[curr_index]:
                    await message.channel.send("Correct!")
                    await send_trivia_question(message)
                else:
                    await message.channel.send("Incorrect! Try again.")
            else:
                await message.channel.send("Please enter a number from 1 to 4.")
        else:
            await message.channel.send("Please enter a number corresponding to the correct solution.")

    elif input_content == "trivia":
        await send_trivia_question(message)
        in_trivia = True




def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
