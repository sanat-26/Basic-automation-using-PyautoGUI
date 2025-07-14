import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="API_KEY")

pyautogui.click(x=8, y=342)
time.sleep(1)
pyautogui.moveTo(593,301)
pyautogui.mouseDown()
pyautogui.moveTo(1351,884, duration = 0.5)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)
pyautogui.click(593,300)
time.sleep(1)
pyautogui.click(21,389)


text = pyperclip.paste()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,
    messages=[
        {"role": "user", "content": 'you are a virtual assisstant named jarvis skilled in general tasks like chatgpt. explain what the text given to you is about.'},
        {'role': 'user', 'content': text}
    ]
)
print(completion.choices[0].message)