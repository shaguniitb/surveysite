from django.forms.widgets import NumberInput, Select

class SelectableButton(Select):
  pass

class RangeInput(NumberInput):
  """A discrete range slider"""
  input_type = 'range'

  def __init__(self, attrs = None, min = 1, max = 5, step = 1):
    self.attrs = {}
    # Set up more attrs
    if 'class' in self.attrs:
      self.attrs['class'] += ' range-slider'
    else:
      self.attrs['class'] = 'range-slider'

    self.attrs['min'] = min
    self.attrs['max'] = max
    self.attrs['step'] = step

    if not attrs is None:
      for key in attrs:
        self.attrs[key] = attrs[key]

class SemanticScale(RangeInput):
  """A semantic differential scale based on a range slider"""
  def __init__(self, attrs = None, levels = 5):
    super().__init__(attrs, min = 1, max = levels, step = 1)
    self.attrs['class'] += 'semantic-scale'
