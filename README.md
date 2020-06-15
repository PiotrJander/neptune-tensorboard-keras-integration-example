# Minimal example showing keras integration to not log metrics

Setup:

1. Create a virtual environment (tested with Python 3.8)
1. `pip install -r requirements.txt` (note that `requirements.txt` refers to
    a `neptune-tensorboard` version from a commit on the Github repo, rather
    than to the version published on Pypi).
1. Set NEPTUNE_API_TOKEN and NEPTUNE_PROJECT.
1. `python example.py`
1. Verify that metrics were not logged.

On the other hand, if you also install `pip install 'Keras==2.3.1'` and therefore
make `neptune-tensorboard` import `keras` through `import keras` rather than
through `import tensorflow.keras`, metrics are logged just fine.

My guess is that the inconsistency is due to our hackish way of modifying Keras
by assigning to a field of an imported object (I have never seen this in other
libraries); see [this file](https://github.com/neptune-ai/neptune-tensorboard/blob/9c91b1f17342e3773071397e812e537ceb73055f/neptune_tensorboard/integration/keras_integration.py#L119).
I also tried doing it like [this](https://github.com/neptune-ai/neptune-tensorboard/blob/ad9f017adcbcda3ef44975e5a9b119ddc30fbcb6/neptune_tensorboard/integration/keras_integration.py#L122), but it doesn't work either.

Perhaps there is something in the way Python imports work that makes our hackish
way of integrating with Keras unpredictable or unintuitive.