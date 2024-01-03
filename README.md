To run tests on Jenkins/Agent container:
1. Build Dockerfile_arm - docker build . --platform=linux/arm64 -t meskman/pytestimg5
2. Push it to DockerHub - docker push meskman/pytestimg5
3. Add meskman/pytestimg5 image to docker cloud on Jenkins