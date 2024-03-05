from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.popup import Popup
import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

class YouTubeDownloader(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.link_input = TextInput(hint_text='Enter YouTube Link', multiline=False)
        layout.add_widget(self.link_input)

        self.convert_button = Button(text='Convert To Audio', size_hint=(None, None), size=(200, 50))
        self.convert_button.bind(on_press=self.download_sound)
        layout.add_widget(self.convert_button)

        return layout

    def download_sound(self, instance):
        try: 
            vid = YouTube(self.link_input.text)
            myStream = vid.streams.first()
            out_file = myStream.download()
            base, ext = os.path.splitext(out_file)
            video = VideoFileClip(out_file)
            audio = video.audio
            video.close()
            print(audio)
            os.rename(out_file, base+".mp3" )
            audio.write_audiofile(base, codec='mp3')  
            

            popup = Popup(title='Success!', content=Label(text='You Have Successfully Downloaded The Audio'), size_hint=(None, None), size=(400, 200))
            popup.open()
        except Exception as e:
            popup = Popup(title='Oops!', content=Label(text=f'You Encountered An Error\nCould be an incorrect link.\nError: {e}'), size_hint=(None, None), size=(400, 200))
            popup.open()

if __name__ == '__main__':
    YouTubeDownloader().run()
