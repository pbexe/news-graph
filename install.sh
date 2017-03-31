# echo '===================================================='
# echo 'Installing requirements'
# echo '===================================================='
# sudo pip3 install -r requirements.txt
echo '===================================================='
echo 'Downloading required NLTK libs'
echo '===================================================='
python -m nltk.downloader -d /usr/local/share/nltk_data stopwords book
cd src/
echo '===================================================='
echo 'Check for DB changes'
echo '===================================================='
python manage.py makemigrations
echo '===================================================='
echo 'Build DB'
echo '===================================================='
python manage.py migrate
echo '===================================================='
echo 'Updating DB'
echo '===================================================='
python updateDB.py
