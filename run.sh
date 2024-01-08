export OVERRIDE_S3_ENDPOINT='http://localhost:9000/'
export BUCKET='STARK_DEV'
export ACCESS_KEY='minioadmin'
export SECRET_KEY='minioadmin'
export REGION='ap-south-1'
export OBJECT_BASE_URL='http://localhost:9000/STARK_DEV/CART_WAVE_DEV/PRODUCTS/'
export JWT_SECRET='rsarkar123456'
export MONGODB_URI='mongodb://localhost:27017/vision_dev'
export TIMEZONE='Asia/Kolkata'

export THRESHOLD=900
export ELECTRICAL_CONN='http://192.168.1.22/'

echo -e "====================== Vision2Reality ========================"
python3 -c "from main import run; run()"