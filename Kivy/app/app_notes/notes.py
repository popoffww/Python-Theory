from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton

class NoteListButton(ListItemButton):
    pass

class NotesBoxLayout(BoxLayout):

    data = ObjectProperty()
    event = ObjectProperty()
    notes_list = ObjectProperty()

    def add_note(self):

        event_note = self.data.text + '   ' + self.event.text

        self.notes_list.adapter.data.extend([event_note])

        self.notes_list._trigger_reset_populate()

    def delete_note(self, *args):

        if self.notes_list.adapter.selection:

            selection = self.notes_list.adapter.selection[0].text

            self.notes_list.adapter.data.remove(selection)

            self.notes_list._trigger_reset_populate()

    def replace_note(self, *args):

        if self.notes_list.adapter.selection:

            selection = self.notes_list.adapter.selection[0].text

            self.notes_list.adapter.data.remove(selection)

            notes_name = self.data.text + '   ' + self.event.text

            self.notes_list.adapter.data.extend([notes_name])

            self.notes_list._trigger_reset_populate()

    def save_note(self, *args):

        if self.notes_list.adapter.selection:

            selection = self.notes_list.adapter.selection[0].text

            self.notes_list.adapter.data.save(selection)

            notes_name = self.data.text + '   ' + self.event.text

            self.notes_list.adapter.data.extend([notes_name])

            self.notes_list._trigger_reset_populate()



class NotesApp(App):
    def build(self):
        return NotesBoxLayout()

if __name__ == '__main__':
    NotesApp().run()
