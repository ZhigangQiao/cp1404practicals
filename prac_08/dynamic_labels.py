from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main Kivy app for dynamically creating labels."""

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        # Sample data - list of names
        self.names = ["Alice", "Bob", "Charlie", "David"]

    def build(self):
        """Build the Kivy app."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels dynamically based on the list of names."""
        for name in self.names:
            # Create a label for each name
            temp_label = Label(text=name)
            # Add the label to the layout
            self.root.ids.labels_box.add_widget(temp_label)


DynamicLabelsApp().run()
