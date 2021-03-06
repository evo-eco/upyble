appe_keys = ['UNKNOWN',
             'GENERIC_PHONE',
             'GENERIC_COMPUTER',
             'GENERIC_WATCH',
             'WATCH_SPORTS_WATCH',
             'GENERIC_CLOCK',
             'GENERIC_DISPLAY',
             'GENERIC_REMOTE_CONTROL',
             'GENERIC_EYE_GLASSES',
             'GENERIC_TAG',
             'GENERIC_KEYRING',
             'GENERIC_MEDIA_PLAYER',
             'GENERIC_BARCODE_SCANNER',
             'GENERIC_THERMOMETER',
             'THERMOMETER_EAR',
             'GENERIC_HEART_RATE_SENSOR',
             'HEART_RATE_SENSOR_HEART_RATE_BELT',
             'GENERIC_BLOOD_PRESSURE',
             'BLOOD_PRESSURE_ARM',
             'BLOOD_PRESSURE_WRIST',
             'GENERIC_HID',
             'HID_KEYBOARD',
             'HID_MOUSE',
             'HID_JOYSTICK',
             'HID_GAMEPAD',
             'HID_DIGITIZERSUBTYPE',
             'HID_CARD_READER',
             'HID_DIGITAL_PEN',
             'HID_BARCODE',
             'GENERIC_GLUCOSE_METER',
             'GENERIC_RUNNING_WALKING_SENSOR',
             'RUNNING_WALKING_SENSOR_IN_SHOE',
             'RUNNING_WALKING_SENSOR_ON_SHOE',
             'RUNNING_WALKING_SENSOR_ON_HIP',
             'GENERIC_CYCLING',
             'CYCLING_CYCLING_COMPUTER',
             'CYCLING_SPEED_SENSOR',
             'CYCLING_CADENCE_SENSOR',
             'CYCLING_POWER_SENSOR',
             'CYCLING_SPEED_CADENCE_SENSOR',
             'GENERIC_PULSE_OXIMETER',
             'PULSE_OXIMETER_FINGERTIP',
             'PULSE_OXIMETER_WRIST_WORN',
             'GENERIC_WEIGHT_SCALE',
             'GENERIC_PERSONAL_MOBILITY_DEVICE',
             'PERSONAL_MOBILITY_DEVICE_POWERED_WHEELCHAIR',
             'PERSONAL_MOBILITY_DEVICE_MOBILITY_SCOOTER',
             'GENERIC_CONTINUOUS_GLUCOSE_MONITOR',
             'GENERIC_INSULIN_PUMP',
             'INSULIN_PUMP_DURABLE_PUMP',
             'INSULIN_PUMP_PATCH PUMP',
             'INSULIN_PUMP_INSULIN_PEN',
             'GENERIC_MEDICATION_DELIVERY',
             'GENERIC_OUTDOOR_SPORTS_ACTIVITY',
             'OUTDOOR_SPORTS_ACTIVITY_LOCATION_DISPLAY_DEVICE',
             'OUTDOOR_SPORTS_ACTIVITY_LOCATION_AND_NAVIGATION_DISPLAY_DEVICE',
             'OUTDOOR_SPORTS_ACTIVITY_LOCATION_POD',
             'OUTDOOR_SPORTS_ACTIVITY_LOCATION_AND_NAVIGATION_POD',
             'GENERIC_ENVIRONMENTAL_SENSOR']

appe_codes = [0,
              64,
              128,
              192,
              193,
              256,
              320,
              384,
              448,
              512,
              576,
              640,
              704,
              768,
              769,
              832,
              833,
              896,
              897,
              898,
              960,
              961,
              962,
              963,
              964,
              965,
              966,
              967,
              968,
              1024,
              1088,
              1089,
              1090,
              1091,
              1152,
              1153,
              1154,
              1155,
              1156,
              1157,
              3136,
              3137,
              3138,
              3200,
              3264,
              3265,
              3266,
              3328,
              3392,
              3393,
              3396,
              3400,
              3456,
              5184,
              5185,
              5186,
              5187,
              5188,
              5696]


ble_appearances_dict = dict(zip(appe_codes, appe_keys))
ble_appearances_dict_rev = dict(zip(appe_keys, appe_codes))
