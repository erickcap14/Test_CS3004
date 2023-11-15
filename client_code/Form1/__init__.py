from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.map = GoogleMap()

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(f'Hello!')

  def map_1_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass

  def map_1_drag(self, **event_args):
    """This method is called This event is repeatedly fired while the user drags the map."""
    pass

  def map_1_data_removeproperty(self, feature, name, old_value, **event_args):
    """This method is called when a feature's property is removed."""
    pass

