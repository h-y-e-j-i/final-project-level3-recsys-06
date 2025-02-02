from typing import List
from collections import OrderedDict
import streamlit as st
import requests
import emoji

def delete_none(datas: dict):
    will_be_removed = []
    for i in OrderedDict(datas):
        print(i)
        if i=='token_id':
            datas['Token ID']=datas.pop(i)
        elif i=='artifact':
            datas['Artifact']=datas.pop(i)
        elif i=='is_artifact':
            datas['Artifact?']=datas.pop(i)
        elif i=='category':
            datas['Category']=datas.pop(i)
        elif i=='eastern_resource':
            datas['Eastern Resource']=datas.pop(i)
        elif i=='environment':
            datas['Environment']=datas.pop(i)
        elif i=='koda_clothing': 
            datas['Koda - Clothing']=datas.pop(i)
        elif i=='is_koda_clothing':
            datas['Koda - Clothing?']=datas.pop(i)
        elif i=='koda_core':
            datas['Koda - Core']=datas.pop(i)
        elif i=='koda_eyes':
            datas['Koda - Eyes']=datas.pop(i)
        elif i=='koda_head':
            datas['Koda - Head']=datas.pop(i)
        elif i=='is_koda_mega':
            datas['Koda - Mega?']=datas.pop(i)
        elif i=='koda_weapon':
            datas['Koda - Weapon']=datas.pop(i)
        elif i=='is_koda_weapon':
            datas['Koda - Weapon?']=datas.pop(i)
        elif i=='koda_id':
            datas['Koda ID']=datas.pop(i)
        elif i=='is_koda':
            datas['Koda?']=datas.pop(i)
        elif i=='northern_resource':
            datas['Northern Resource']=datas.pop(i)
        elif i=='sediment':
            datas['Sediment']=datas.pop(i)
        elif i=='southern_resource':
            datas['Southern Resource']=datas.pop(i)
        elif i=='western_resource':
            datas['Western Resource']=datas.pop(i)
        elif i=='environment_tier':
            datas['Environment Tier']=datas.pop(i)
        elif i=='koda':
            datas['Koda']=datas.pop(i)
        elif i=='northern_resource_tier':
            datas['Northern Resource Tier']=datas.pop(i)
            break
        elif i=='sediment_tier':
            datas['Sediment Tier']=datas.pop(i)
        elif i=='southern_resource_tier':
            datas['Southern Resource Tier']=datas.pop(i)
        elif i=='western_resource_tier':
            datas['Western Resource Tier']=datas.pop(i)
        elif i=='eastern_resource_tier':
            datas['Eastern Resource Tier']=datas.pop(i)
        else:
            continue
            
    for data in datas:
        if data == 'eastern_resource_tier':
            datas['eastern_resource_tier'] = datas['eastern_resource_tier'].strip()

        if not datas[data]:
            will_be_removed.append(data)
        
    for i in will_be_removed:
        datas.pop(i)
    
    

def get_related_tokens(datas: dict):
    related_token_list = ['token_id_1','token_id_2','token_id_3','token_id_4','token_id_5',
                                    'token_id_6','token_id_7','token_id_8','token_id_9','token_id_10',]
    related_tokens = []
    for related_token in related_token_list:
        related_tokens.append(datas.pop(related_token))
    return related_tokens

def get_real_value(datas: dict):
    if datas['Seller_price_type']=='Ether':
        datas['Seller_price_type']='ETH'
    elif datas['Seller_price_type']=='Wrapped Ether':
        datas['Seller_price_type']='WETH'
    else:
        datas['Seller_price_type']='ETH'
        datas['Seller_price']=0
    if datas['Buyer_price_type']=='Ether':
        datas['Buyer_price_type']='ETH'
    elif datas['Buyer_price_type']=='Wrapped Ether':
        datas['Buyer_price_type']='WETH'
    else:
        datas['Buyer_price_type']='ETH'
        datas['Buyer_price']=0
    return datas

def get_image_url(datas: dict):
    return datas.pop('image_original_url')

def get_token_id(datas: dict):
    return datas.pop('token_id')

def get_expected_price(datas: dict):
    return datas.pop('price')

def get_predicted_value(datas: dict):
    return datas.pop('predict_value')

def increment_counter(num):
    st.session_state.token_num += 1
    st.session_state.idx=num
    
def decreasement_counter(num):
    st.session_state.token_num -= 1
    st.session_state.idx=num
    
def change_idx(num): 
    st.session_state.idx=num

def change_counter(num): 
    st.session_state.token_num=num

def change_both(index, num):
    st.session_state.idx=num
    st.session_state.token_num=index

st.set_page_config(
    # layout="wide",
    initial_sidebar_state="expanded",    # 사이드바 상태 : auto / expanded / collapsed
    page_title='NFTeam',
    page_icon='https://upload.wikimedia.org/wikipedia/commons/2/24/NFT_Icon.png?20191215204608'
    )
 
if 'NFT_name' not in st.session_state:
    st.session_state.NFT_name='Main'
    st.session_state.idx = -1
# sidebar
st.session_state.NFT_name = st.sidebar.selectbox('Please select in selectbox!',
        ('Main','Otherdeed for Otherside', 'Azuki', 'Bored Ape Yacht Club','Test'))
if st.session_state.NFT_name == 'Main':
    st.header('[ NFT Collections ]')
    st.write('')
    st.write('')
    st.write('')
    Main_column0=st.columns(2)
    with Main_column0[0]:
        st.subheader('Otherdeed for Otherside')
        st.image('https://lh3.googleusercontent.com/yIm-M5-BpSDdTEIJRt5D6xphizhIdozXjqSITgK4phWq7MmAU3qE7Nw7POGCiPGyhtJ3ZFP8iJ29TFl-RLcGBWX5qI4-ZcnCPcsY4zI=s168')
    with Main_column0[1]:
        st.subheader('Azuki')
        st.image('https://lh3.googleusercontent.com/H8jOCJuQokNqGBpkBN5wk1oZwO7LM8bNnrHCaekV2nKjnCqw6UB5oaH8XyNeBDj6bA_n1mjejzhFQUP3O1NfjFLHr3FOaeHcTOOT=s168')
    Main_column1=st.columns(2)
    with Main_column1[0]:
        st.subheader('Bored Ape Yacht Club')
        st.image('https://lh3.googleusercontent.com/Ju9CkWtV-1Okvf45wo8UctR-M9He2PjILP0oOvxE89AyiPPGtrR3gysu1Zgy0hjd2xKIgjJJtWIc0ybj4Vd7wv8t3pxDGHoJBzDB=s168')

if st.session_state.NFT_name == 'Otherdeed for Otherside':
    if 'token_num' not in st.session_state:
        st.session_state.token_num = -1
    title_col=st.columns((1,4))
    with title_col[0]:
        st.image('https://lh3.googleusercontent.com/yIm-M5-BpSDdTEIJRt5D6xphizhIdozXjqSITgK4phWq7MmAU3qE7Nw7POGCiPGyhtJ3ZFP8iJ29TFl-RLcGBWX5qI4-ZcnCPcsY4zI=s168')
    with title_col[1]:
        st.write('')
        st.write('')
        st.title("Otherdeed for Otherside")
    ordinal_number = ['첫', '두', '세', '네', '다섯', '여섯', '일곱', '여덟', '아홉', '열']
    st.write('')
    st.write('')

    select_c=st.columns((4,1))
    with select_c[0]:
        st.session_state.select_text = st.text_input(label = 'Token ID', placeholder = '숫자를 입력해주세요~')
    with select_c[1]:
        st.write('')
        st.write('')
        st.write('')
        st.session_state.select_button = st.button('Search', on_click=change_idx, args=(st.session_state.select_text,))
    if st.session_state.select_button : # search 버튼을 누르면
        try:
            val  = int(st.session_state.select_text)
            if 0 <= val < 100000: # 범위를 벗어난다면 
                st.session_state.token_num = 10
            else:
                st.session_state.token_num=-1
                st.warning('해당 Token_id가 없습니다. 다시 입력해주세요.')
        except:
            st.session_state.token_num=-1
            st.warning('숫자를 입력해주세요')

    if st.session_state.token_num==10:
        if 'idx' not in st.session_state:
            st.session_state.idx = st.session_state.select_text 

        token_info = requests.get(f"http://localhost:30002/token/{st.session_state.idx}").json()
        related_tokens = get_related_tokens(token_info)
        delete_none(token_info)
        image_link = get_image_url(token_info)
        predict_value = get_predicted_value(token_info)
        real_value = requests.get(f"http://localhost:30002/price/{st.session_state.idx}").json()
        real_value = get_real_value(real_value)
        
        st.header(f"[ #{st.session_state.idx} ]에 대한 정보입니다.")
        st.subheader(f"판매 가격 : {real_value['Seller_price']:.3f} {real_value['Seller_price_type']} / offer 가격 : {real_value['Buyer_price']:.3f} {real_value['Buyer_price_type']}")
        
        if predict_value>max(real_value['Seller_price'],real_value['Buyer_price']):
            st.markdown(f"**<font size='6'>▶ 예측 가격 : <span style='color:#6067d0'>{predict_value:.3f}</span> ETH</font>**",unsafe_allow_html=True)
        else:
            st.markdown(f"**<font size='6'>▶ 예측 가격 : <span style='color:#ff6265'>{predict_value:.3f}</span> ETH</font>**",unsafe_allow_html=True)
        
        # if predict_value>max(real_value['Seller_price'],real_value['Buyer_price']):
        #     st.success(f"예측 가격 : {predict_value:.3f} ETH")
        # else:
        #     st.error(f"예측 가격 : {predict_value:.3f} ETH")
            
        main_c = st.columns(2)
        with main_c[0]:
            st.image(image_link)
            
        with main_c[1]:
            for a in token_info.keys():
                st.write(f' - {a} : {token_info[a]}')
        back_col=st.columns(8)
        
        with back_col[7]:
            st.session_state.back_button=st.button('Back',on_click=change_counter,args=(-1,))

        # 유사한 아이템 보여주기
        st.write('')
        st.write('')
        st.subheader('[ 비슷한 NFT들 ]')
        query = "http://localhost:30002/tokens/?"
        for token in related_tokens:
            query += f'token_ids={token}&'
        temp = requests.get(query).json()

        # col0, col1, col2, col3, col4 = st.columns(5)
        col_first = list(st.columns(5))
        for first, col in enumerate(col_first):
            with col:
                st.session_state.first=st.button(label=f'#{related_tokens[first]}', on_click=change_idx, args=(related_tokens[first],))
                st.image(temp[first]['image_original_url'])
        
        col_second = list(st.columns(5))
        for second, col in enumerate(col_second):
            with col:
                st.session_state.second=st.button(label=f'#{related_tokens[second+5]}', on_click=change_idx, args=(related_tokens[second+5],))
                st.image(temp[second+5]['image_original_url'])

    elif (st.session_state.token_num >= 0) and (st.session_state.token_num <= 9):
        today_recommends = requests.get(f"http://localhost:30002/Top10").json() # Top 10 개를 불러온다.

        token_info = requests.get(f"http://localhost:30002/token/{st.session_state.idx}").json() # Top 10 개의 정보를 가지고 온다.
        related_tokens = get_related_tokens(token_info)
        delete_none(token_info)
        image_link = get_image_url(token_info)
        predict_value = get_predicted_value(token_info)
        real_value = requests.get(f"http://localhost:30002/price/{st.session_state.idx}").json()
        real_value = get_real_value(real_value)
        
        st.header(f'오늘의 {ordinal_number[st.session_state.token_num]} 번째 추천 [ #{today_recommends[st.session_state.token_num]} ]')
        st.subheader(f"판매 가격 : {real_value['Seller_price']:.3f} {real_value['Seller_price_type']} / offer 가격 : {real_value['Buyer_price']:.3f} {real_value['Buyer_price_type']}")
        
        if predict_value>max(real_value['Seller_price'],real_value['Buyer_price']):
            st.markdown(f"**<font size='6'>▶ 예측 가격 : <span style='color:#6067d0'>{predict_value:.3f}</span> ETH</font>**",unsafe_allow_html=True)
        else:
            st.markdown(f"**<font size='6'>▶ 예측 가격 : <span style='color:#ff6265'>{predict_value:.3f}</span> ETH</font>**",unsafe_allow_html=True)
            
        main_c = st.columns(2)
        with main_c[0]:
            st.image(image_link)
        with main_c[1]:
            for a in token_info.keys():
                st.write(f' - {a} : {token_info[a]}')
        sub_c = st.columns((4, 3, 3))
        with sub_c[0]:
            if st.session_state.token_num !=0:
                left_button = st.button(
                    label="이전", disabled=(st.session_state.token_num <= -1),
                    on_click=decreasement_counter, args=(today_recommends[st.session_state.token_num-1],)
                )
        with sub_c[1]:
            if st.session_state.token_num != 9:
                right_button = st.button(
                    label="다음", disabled=(st.session_state.token_num >= len(ordinal_number)),
                    on_click=increment_counter, args=(today_recommends[st.session_state.token_num+1],)
                )
        
    if st.session_state.token_num != 10:
        st.write('')
        st.write('')
        st.subheader('[ 이 시각 추천 NFT ]')
        today_recommends = requests.get(f"http://localhost:30002/Top10").json() # 오늘의 추천 10개를 리스트로 받아옴
        query = "http://localhost:30002/tokens/?" # Ex) http://localhost:30002/tokens/?token_ids=22&token_ids33... 
        for token in today_recommends:
            query += f'token_ids={token}&'
        recommended = requests.get(query).json() # 추천 받은 10개의 모든 정보를 받아온다.
        
        col_third = list(st.columns(5))
        for third, col in enumerate(col_third):
            with col:
                st.session_state.third=st.button(label=f"#{recommended[third]['token_id']}", on_click=change_both, args=(third, recommended[third]['token_id'],))
                st.image(recommended[third]['image_original_url'])
            
        col_forth = list(st.columns(5))
        for forth, col in enumerate(col_forth):
            with col:
                st.session_state.forth=st.button(label=f"#{recommended[forth+5]['token_id']}", on_click=change_both, args=(forth+5, recommended[forth+5]['token_id'],))
                st.image(recommended[forth+5]['image_original_url'])