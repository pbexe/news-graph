echo '===================================================='
echo 'Installing requirements'
echo '===================================================='
sudo pip3 install -r requirements.txt
echo '===================================================='
echo 'Downloading required NLTK libs'
echo '===================================================='
sudo python3 -m nltk.downloader -d /usr/local/share/nltk_data stopwords
cd src/
echo '===================================================='
echo 'Updating DB'
echo '===================================================='
python3 updateDB.py