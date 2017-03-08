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
echo 'Check for DB changes'
echo '===================================================='
python3 manage.py makemigrations
echo '===================================================='
echo 'Build DB'
echo '===================================================='
python3 manage.py migrate
echo '===================================================='
echo 'Updating DB'
echo '===================================================='
python3 updateDB.py
read -n 1 -s -p "Press any key to continue"