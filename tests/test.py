import re

script = """
import tf_utils
import tensorflow as tf

def placeholder(P, Q, N):
    X = tf.compat.v1.placeholder(
        shape=(None, P, N), dtype=tf.float32, name='X')
    TE = tf.compat.v1.placeholder(
        shape=(None, P + Q, 2), dtype=tf.int32, name='TE')
    label = tf.compat.v1.placeholder(
        shape=(None, Q, N), dtype=tf.float32, name='label')
    is_training = tf.compat.v1.placeholder(
        shape=(), dtype=tf.bool, name='is_training')
    return X, TE, label, is_training

def FC(x, units, activations, bn, bn_decay, is_training, use_bias=True, drop=None):
    if isinstance(units, int):
        units = [units]
        activations = [activations]
    elif isinstance(units, tuple):
        units = list(units)
        activations = list(activations)
    assert type(units) == list
    for num_unit, activation in zip(units, activations):
        if drop is not None:
            x = tf_utils.dropout(x, drop=drop, is_training=is_training)
        x = tf_utils.conv2d(
            x, output_dims=num_unit, kernel_size=[1, 1], stride=[1, 1],
            padding='VALID', use_bias=use_bias, activation=activation,
            bn=bn, bn_decay=bn_decay, is_training=is_training)
    return x
"""

# Define the pattern for separating import and script
pattern = re.compile(r'(?<=\bdef\b)', re.DOTALL | re.MULTILINE)

# Find the first occurrence of a function definition
match = pattern.search(script)

if match:
    # Extract import and script parts
    import_part = script[: match.start()]
    script_part = script[match.start():]

    # Print the results
    print("Import Part:")
    print(import_part)

    print("\nScript Part:")
    print(script_part)
else:
    print("No function definition found.")
