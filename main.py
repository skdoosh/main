# Batch Gradient Descent for Medical Image Classification
# Small Dataset: 10 Normal + 10 Pneumonia Images

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# ----------------------------------------
# 1. LOAD DATASET
# ----------------------------------------

IMG_SIZE = 64
BATCH_SIZE = 20

train_path = "dataset/train/"
test_path = "dataset/test/"

datagen = ImageDataGenerator(rescale=1./255)

train_data = datagen.flow_from_directory(
        train_path,
            target_size=(IMG_SIZE, IMG_SIZE),
                batch_size=BATCH_SIZE,
                    class_mode='binary'
)

test_data = datagen.flow_from_directory(
        test_path,
            target_size=(IMG_SIZE, IMG_SIZE),
                batch_size=BATCH_SIZE,
                    class_mode='binary'
)

# ----------------------------------------
# 2. BUILD SIMPLE CNN MODEL
# ----------------------------------------

model = models.Sequential([

        layers.Conv2D(16, (3,3), activation='relu',
                          input_shape=(IMG_SIZE, IMG_SIZE, 3)),

                              layers.MaxPooling2D(2,2),

                                  layers.Flatten(),

                                      layers.Dense(32, activation='relu'),

                                          layers.Dense(1, activation='sigmoid')
])

# ----------------------------------------
# 3. BATCH GRADIENT DESCENT OPTIMIZER
# ----------------------------------------

optimizer = tf.keras.optimizers.SGD(
        learning_rate=0.01
)

model.compile(
        optimizer=optimizer,
            loss='binary_crossentropy',
                metrics=['accuracy']
)

# ----------------------------------------
# 4. TRAIN MODEL
# ----------------------------------------

model.fit(
        train_data,
            epochs=10
)

# ----------------------------------------
# 5. TEST MODEL
# ----------------------------------------

loss, accuracy = model.evaluate(test_data)

print("Test Accuracy:", accuracy)

# ----------------------------------------
# 6. SAVE MODEL
# ----------------------------------------

model.save("medical_model.h5")

print("Training Complete")# Batch Gradient Descent for Medical Image Classification
# Small Dataset: 10 Normal + 10 Pneumonia Images

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models

# ----------------------------------------
# 1. LOAD DATASET
# ----------------------------------------

IMG_SIZE = 64
BATCH_SIZE = 20

train_path = "dataset/train/"
test_path = "dataset/test/"

datagen = ImageDataGenerator(rescale=1./255)

train_data = datagen.flow_from_directory(
        train_path,
            target_size=(IMG_SIZE, IMG_SIZE),
                batch_size=BATCH_SIZE,
                    class_mode='binary'
)

test_data = datagen.flow_from_directory(
        test_path,
            target_size=(IMG_SIZE, IMG_SIZE),
                batch_size=BATCH_SIZE,
                    class_mode='binary'
)

# ----------------------------------------
# 2. BUILD SIMPLE CNN MODEL
# ----------------------------------------

model = models.Sequential([

        layers.Conv2D(16, (3,3), activation='relu',
                          input_shape=(IMG_SIZE, IMG_SIZE, 3)),

                              layers.MaxPooling2D(2,2),

                                  layers.Flatten(),

                                      layers.Dense(32, activation='relu'),

                                          layers.Dense(1, activation='sigmoid')
])

# ----------------------------------------
# 3. BATCH GRADIENT DESCENT OPTIMIZER
# ----------------------------------------

optimizer = tf.keras.optimizers.SGD(
        learning_rate=0.01
)

model.compile(
        optimizer=optimizer,
            loss='binary_crossentropy',
                metrics=['accuracy']
)

# ----------------------------------------
# 4. TRAIN MODEL
# ----------------------------------------

model.fit(
        train_data,
            epochs=10
)

# ----------------------------------------
# 5. TEST MODEL
# ----------------------------------------

loss, accuracy = model.evaluate(test_data)

print("Test Accuracy:", accuracy)

# ----------------------------------------
# 6. SAVE MODEL
# ----------------------------------------

model.save("medical_model.h5")

print("Training Complete")
)
)
)
])
)
)
)
)
)
])
)
)