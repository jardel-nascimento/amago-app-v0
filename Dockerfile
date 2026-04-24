FROM kivy/buildozer

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

COPY . /app

RUN python3 -m pip install --no-cache-dir "Cython==0.29.36"
