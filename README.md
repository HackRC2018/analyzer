# Install
```
# Create a virtualenv
virtualenv venv -p python

# Activate it
source venv/bin/activate

# Install depenndencies
pip install -r requirements.txt
```

# Download french data for polyglot
```
source setup_post_requirements.sh
```

# Linux
```
sudo apt-get install python-numpy libicu-dev
```

# Mac
```
brew install icu4c
brew link icu4c --force
pip install pyicu
```

# Launch the script
```
python script.py
```

# Docker
```
docker build -t analyzer .
docker run -d \
    --name analyzer \
    --link podcast-mongo:mongo \
    -e 'MONGODB_HOST=mongo' \
    analyzer
```