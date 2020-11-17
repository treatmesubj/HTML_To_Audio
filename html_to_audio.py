import os
from bs4 import BeautifulSoup
import pyttsx3
# from gtts import gTTS
# # from gtts_token.gtts_token import Token


# class resolute_Token(Token):
# 	def __init__(self):
# 		super().__init__()

# 	def calculate_token(self, *args, **kwargs):
# 		while True:
# 			try:
# 				super().calculate_token(*args, **kwargs)
# 				break
# 			except Exception as e:
# 				if "Unable to find token seed" in str(e):
# 					pass
# 				else:
# 					raise e


# class resolute_gTTS(gTTS):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.token = resolute_Token()


def html_to_audio(file_path):
	with open(file_path, encoding="utf-8") as f:
		html = f.read()
	soup = BeautifulSoup(html, 'html.parser')
	file_text = " ".join(paragraph.text for paragraph in soup.select("p"))
	
	engine = pyttsx3.init(); engine.setProperty('rate', 200)
	engine.save_to_file(file_text, f"{os.path.splitext(file_path)[0]}.mp3")
	engine.runAndWait()

	print(f"{file_path} done...")


	# speech = resolute_gTTS(text=file_text)
	# speech.save(f"{os.path.splitext(file_path)[0]}.mp3")

if __name__ == "__main__":

	while True:
		choice = input("['dir'|'file']: ")
		if choice in ["dir", "file"]:
			break

	if choice == "dir":
		directory = input("book directory: ").strip("\"")
		for chapter_file in os.listdir(directory):
			html_to_audio(os.path.join(directory, chapter_file))

	if choice == "file":
		file_path = input("file-path: ").strip("\"")
		html_to_audio(file_path)
