import tensorflow as tf
import warnings

class Conv:
    def __init__(self):
        if self.debug_gpu():
            print("Using GPU")
        else:
            warnings.warn("GPU not found. Defaulting to CPU\nModel should still train but may be slow", UserWarning)

        self.model = self.new_model()

    # Debug GPU info | True if GPU installed
    def debug_gpu(self):
        devices = tf.config.list_physical_devices()
        print("\nDevices: ", devices)

        gpus = tf.config.list_physical_devices("GPU")
        if gpus:
            details = tf.config.experimental.get_device_details(gpus[0])
            print("GPU details: ", details)

        return gpus

    def new_model(self, input_shape=(4032, 4032)):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Input(shape=input_shape),

            tf.keras.layers.Conv2D(filters=256, kernel_size=(3, 3), activation="relu", padding="same"),
            tf.keras.layers.BatchNormalization(),
            tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
            tf.keras.layers.Dropout(0.3),

            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(64, activation="relu"),
            #tf.keras.layers.Dense(num_classes, activation="softmax")
        ])

        return model


if __name__ == "__main__":
    conv = Conv()