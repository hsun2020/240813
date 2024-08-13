import streamlit as st
from PIL import Image

# 식물 정보 데이터베이스 (예시)
plant_info = {
    'rose': {
        'name': '장미',
        'features': '장미는 아름다운 꽃을 피우며, 다양한 색상과 향기를 가지고 있습니다.',
        'care': '햇빛이 잘 드는 곳에서 키우고, 물은 적당히 주어야 합니다.'
    },
    'sunflower': {
        'name': '해바라기',
        'features': '해바라기는 큰 노란 꽃을 피우며, 태양을 따라 움직이는 특징이 있습니다.',
        'care': '햇빛이 많이 드는 곳에서 키우고, 물을 충분히 주어야 합니다.'
    },
    'cactus': {
        'name': '선인장',
        'features': '선인장은 가시가 많고, 물을 적게 필요로 합니다.',
        'care': '햇빛이 잘 드는 곳에서 키우고, 물은 아주 가끔씩만 주어야 합니다.'
    }
}

st.title('식물 정보 서비스 🌿')

# 사용자로부터 이미지 파일을 입력받기
uploaded_file = st.file_uploader("이미지 파일을 업로드 해주세요!", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # 이미지를 화면에 표시
    image = Image.open(uploaded_file)
    st.image(image, caption='업로드한 이미지', use_column_width=True)

    # 여기서는 간단히 파일 이름을 기준으로 식물 정보를 출력하는 예시를 보여줍니다.
    # 실제로는 이미지 인식 모델을 사용하여 식물 종류를 판별해야 합니다.
    file_name = uploaded_file.name.lower()

    if 'rose' in file_name:
        plant = 'rose'
    elif 'sunflower' in file_name:
        plant = 'sunflower'
    elif 'cactus' in file_name:
        plant = 'cactus'
    else:
        plant = None

    if plant:
        st.write(f"**식물 이름:** {plant_info[plant]['name']}")
        st.write(f"**특징:** {plant_info[plant]['features']}")
        st.write(f"**잘 기르는 법:** {plant_info[plant]['care']}")
    else:
        st.write("식물 정보를 찾을 수 없습니다. 다른 이미지를 업로드 해주세요.")
