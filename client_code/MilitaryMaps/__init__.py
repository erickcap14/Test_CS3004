from ._anvil_designer import MilitaryMapsTemplate
from anvil import *

class MilitaryMaps(MilitaryMapsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def NewButton_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('MilitaryMaps.Map')
