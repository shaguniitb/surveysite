from django.forms.widgets import NumberInput

class RangeInput(NumberInput):
  input_type = 'range'

  def __init__(self, attrs = None, min = 1, max = 5, step = 1):
    self.attrs = {}
    # Set up more attrs
    self.attrs['class'] = 'range-slider'
    self.attrs['min'] = min
    self.attrs['max'] = max
    self.attrs['step'] = step

    if not attrs is None:
      for key in attrs:
        self.attrs[key] = attrs[key]
