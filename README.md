# Minimal example showing keras integration to not log metrics

Setup:

1. Create a virtual environment (tested with Python 3.8)
1. Check out the `modified-tf` branch.
1. `pip install -r requirements.txt`
1. Set NEPTUNE_API_TOKEN and NEPTUNE_PROJECT.
1. `python example.py`
1. Verify that metrics were not logged.

On the other hand, if you check out the `modified-keras` branch, which differs
only in that `Keras==2.3.1` is included in `requirements.txt` and therefore
`neptune-tensorboard` imports keras through `import keras` rather than through
`import tensorflow.keras`, metrics are logged just fine.

