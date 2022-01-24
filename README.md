# sidepulling-aws
Prevention of Side Pulling Using AWS Cloud and OpenCV 

To reduce the accidents that occurs because of side pulling we have come up with a method to warn the crane handler and the people nearby. This device will have a Node Camera attached it using which photos of the surface below the hoist will be taken each second. And each time a photo is taken it will be sent to the cloud. In the cloud, using OpenCV we will detect the occurrence of side pulling if it happens. To detect this, we will be applying machine learning Algorithms in OpenCV. If a side pulling is detected a message is instantaneously sent to the crane handler from the cloud and a buzzer beep to warn the people nearby
