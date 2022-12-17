import streamlit as st
import pandas as pd
import ast
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import glob

add_selectbox = st.selectbox(
    "Chọn phương pháp chẩn đoán",
    ("Thủ công","Hình ảnh")
)
if add_selectbox == 'Thủ công':
   st.header('HÃY CHỌN BIỂU HIỆN')
   options_trai, options_canh, options_hoa, options_la, options_than, options_re = [],[],[],[],[],[]
   tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Lá", "Thân", "Cành","Trái","Rễ","Hoa"])

   with tab1:
      col1, col2, col3 = st.columns(3)
      col1.image('https://agriplusvn.com/wp-content/uploads/2019/04/70975485_2546076575454577_8207840780790792192_n.jpg', width=230, use_column_width=550)
      a = col1.checkbox('Lá xuất hiện những chấm nhỏ màu vàng')
      if a:options_la = options_la + ['Lá xuất hiện những chấm nhỏ màu vàng']
      col2.image("http://vidanvn.com/oamaglah/2020/12/bo-tri-sau-rieng-2.jpg", width=230, use_column_width=550)
      c = col2.checkbox('Lá ít xanh, có màu sáng bạc')
      if c:options_la = options_la + ['Lá ít xanh, có màu sáng bạc']
      col2.image("https://tapdoanvinasa.com/wp-content/uploads/2022/12/bo-tri-gay-hai-tren-sau-rieng-tap-doan-vinasa-com-3.jpg", width=230, use_column_width=550)
      d = col2.checkbox('Lá quăn queo')
      if d:options_la = options_la + ['Lá quăn queo']
      col1.image("https://tapdoanvinasa.com/wp-content/uploads/2022/04/ray-xanh-tren-cay-sau-rieng-1.jpg", width=230, use_column_width=550)
      b = col1.checkbox('Lá bị khô dần và rụng, mép lá bị cháy xoăn lại')
      if b:options_la = options_la + ['Lá bị khô dần và rụng, mép lá bị cháy xoăn lại']
      col2.image("https://bvtvthienbinh.com/files/upload/thong-tin-dich-hai/nhen-do-hai-sau-rieng-va-bien-phap-phong-tru-02.jpg", width=230, use_column_width=550)
      e = col2.checkbox('Mặt dưới lá tạo thành những chấm đỏ li ti')
      if e:options_la = options_la + ['Mặt dưới lá tạo thành những chấm đỏ li ti']
      col3.image("https://www.hoptri.com/images/quytrinhgiaiphap/2021/NhenDoHaiSauRieng/LaSauRiengChuyenMau_02.png", width=230, use_column_width=550)
      f = col3.checkbox('Lá chuyển sang màu vàng xám (giống như có lớp bụi bám trên bề mặt), lá khô và rụng dần')
      if f:options_la = options_la + ['Lá chuyển sang màu vàng xám (giống như có lớp bụi bám trên bề mặt), lá khô và rụng dần']
      col1.image("https://i.ex-cdn.com/nongnghiep.vn/files/f1/2019/7/25/07-40-08_thnthusurieng.jpg", width=230, use_column_width=550)
      g = col1.checkbox('Lá khô cháy dần và rụng sớm')
      if g:options_la = options_la + ['Lá khô cháy dần và rụng sớm']
      col3.image("https://fc-ktr-discourse-production.s3.dualstack.ap-southeast-1.amazonaws.com/optimized/3X/1/c/1ca8ca681d41e42a237e0b782e8965b5e47e913d_2_781x1024.jpeg", width=230, use_column_width=550)
      j = col3.checkbox('Trên lá xuất hiện các đường viền hình tròn có màu nâu đậm dọc theo hai bên gân chính')
      if j:options_la = options_la + ['Trên lá xuất hiện các đường viền hình tròn có màu nâu đậm dọc theo hai bên gân chính']
      col2.image("https://nongnghiepthuanthien.vn/wp-content/uploads/2021/05/sau-rieng-chay-la.jpg", width=230, use_column_width=550)
      l = col2.checkbox('Lá màu xanh nhợt nhạt, sũng nước')
      if l:options_la = options_la + ['Lá màu xanh nhợt nhạt, sũng nước']
      col2.image("https://i.ex-cdn.com/nongnghiep.vn/files/bao_in/2020/04/19/anh-1-0742_20200419_805-100932.jpeg", width=230, use_column_width=550)
      m = col2.checkbox('Trên lá xuất hiện những đốm màu nâu sáng với viền màu nâu tối')
      if m:options_la = options_la + ['Trên lá xuất hiện những đốm màu nâu sáng với viền màu nâu tối']
      col3.image("https://agriplusvn.com/wp-content/uploads/2020/04/Benh-Dom-Rong-hai-Sau-Rieng.jpg", width=230, use_column_width=550)
      n = col3.checkbox('Trên lá xuất hiện đốm màu đỏ rỉ sắt, bề mặt như lớp nhung mịn hơi nhô lên mặt lá')
      if n:options_la = options_la + ['Trên lá xuất hiện đốm màu đỏ rỉ sắt, bề mặt như lớp nhung mịn hơi nhô lên mặt lá']
      col1.image("https://tincay.com/wp-content/uploads/2022/02/tao-Cephaleuros-virescens-gay-benh-dom-rong.jpg", width=230, use_column_width=550)
      o = col1.checkbox('Dưới mặt lá thấy mô lá bị hoại và các sợi tảo mọc xuyên qua có màu đỏ nâu')
      if o:options_la = options_la + ['Dưới mặt lá thấy mô lá bị hoại và các sợi tảo mọc xuyên qua có màu đỏ nâu']

   with tab2:
      col4, col5, col6 = st.columns(3)
      col6.image("https://giongcayeakmat.com/wp-content/uploads/2019/06/sau-duc-than-sau-rieng-2.jpg", width=230, use_column_width=550)
      a_2 = col6.checkbox('Thân cây có những lỗ nhỏ, xung quanh miệng lỗ có lớp bột màu nâu như mùn cưa')
      if a_2: options_than = options_than + ['Thân cây có những lỗ nhỏ, xung quanh miệng lỗ có lớp bột màu nâu như mùn cưa']
      col5.image("https://tamvietagri.vn/wp-content/uploads/2020/06/benh-xi-mu-kho-tren-sau-rieng-3.jpg", width=230, use_column_width=550)
      b_2 = col5.checkbox('Vỏ ngoài thân cây có sự đổi màu nâu vàng hoặc đen sạm tại những lỗ nhỏ')
      if b_2: options_than = options_than + ['Vỏ ngoài thân cây có sự đổi màu nâu vàng hoặc đen sạm tại những lỗ nhỏ']
      col6.image("http://tamvietagri.vn/wp-content/uploads/2020/06/benh-xi-mu-uot-tren-sau-rieng.jpeg", width=230, use_column_width=550)
      c_2 = col6.checkbox('Trên thân xuất hiện vết nứt hoặc chảy nhựa')
      if c_2: options_than = options_than + ['Trên thân xuất hiện vết nứt hoặc chảy nhựa']
      col4.image("https://agriplusvn.com/wp-content/uploads/2020/07/z1975286493402_1d4befcaca70c5934ddf9707a0005949.jpg", width=230, use_column_width=550)
      d_2 = col4.checkbox('Trên vỏ cây hình thành lớp nấm dạng phấn hồng bao phủ bên ngoài')
      if d_2: options_than = options_than + ['Trên vỏ cây hình thành lớp nấm dạng phấn hồng bao phủ bên ngoài']
      col5.image("https://congnghesinhhocwao.vn/wp-content/uploads/2020/03/benh-nam-hong-tren-cay-sau-rieng_optimized.jpg", width=230, use_column_width=550)
      e_2 = col5.checkbox('Vỏ cây bị thâm và thối')
      if e_2: options_than = options_than + ['Vỏ cây bị thâm và thối']

   with tab3:
      col7, col8, col9 = st.columns(3)
      col9.image("https://agriplusvn.com/wp-content/uploads/2019/04/70662266_2546076532121248_8754913580148588544_n.jpg", width=230, use_column_width=550)
      a_3 = col9.checkbox('Trơ cành')
      if a_3: options_canh = options_canh + ['Trơ cành']
      col7.image("https://agriplusvn.com/wp-content/uploads/2020/07/z1975286505772_a484980f279d101b45846a73347525f5-768x1024-min.jpg", width=230, use_column_width=550)
      d_3 = col7.checkbox('Cành bị khô, nứt vỏ')
      if d_3: options_canh = options_canh + ['Cành bị khô, nứt vỏ']
      col8.image("https://nongnghiepthuanthien.vn/wp-content/uploads/2020/10/bieu-hien-ray-xanh-gay-hai-min.jpg", width=230, use_column_width=550)
      e_3 = col8.checkbox('Đọt non bị khô')
      if e_3: options_canh = options_canh + ['Đọt non bị khô']
      col8.image("https://biosacotec.com/wp-content/uploads/2021/12/trieu-chung-sau-rieng-con-bi-kho-dot.jpg", width=230, use_column_width=550)
      h = col8.checkbox('Chết ngọn')
      if h:options_canh = options_canh + ['Chết ngọn']

   with tab4:
      col10, col11, col12 = st.columns(3)
      col10.image("https://www.hoptri.com/media/k2/items/cache/5189f3286915715b50cff89ddded1008_XL.jpg", width=230, use_column_width=550)
      a_4 = col10.checkbox('Trên trái xuất hiện phân đùn ra ngoài qua lỗ đục')
      if a_4: options_trai = options_trai + ['Trên trái xuất hiện phân đùn ra ngoài qua lỗ đục']
      col11.image("https://tapdoanvinasa.com/wp-content/uploads/2022/04/226128000_319239353272438_2503585747517461272_n-1.jpg", width=230, use_column_width=550)
      b_4 = col11.checkbox('Trái bị thối, chỗ thối chuyển sang màu nâu đen')
      if b_4: options_trai = options_trai + ['Trái bị thối, chỗ thối chuyển sang màu nâu đen']
      col12.image("https://agriplusvn.com/wp-content/uploads/2020/04/90001500_2920847637977467_5499017989673975808_o-1-1.jpg", width=230, use_column_width=550)
      c_4 = col12.checkbox('Trái bị biến dạng và rụng')
      if c_4: options_trai = options_trai + ['Trái bị biến dạng và rụng']
      col11.image("https://nongnghiepthuanthien.vn/wp-content/uploads/2022/07/thoi-trai-sau-rieng.jpg", width=230, use_column_width=550)
      d_4 = col11.checkbox('Thối quả')
      if d_4: options_trai = options_trai + ['Thối quả']
      col12.image("https://vietnamnongnghiepsach.com.vn/wp-content/uploads/2018/07/benh-thoi-trai-sau-rieng-1-1.jpg", width=230, use_column_width=550)
      f_4 = col12.checkbox('Trên trái xuất hiện đốm đen nhỏ sũng nước, xuất hiện nấm tạo thành một lớp màu trắng xám')
      if f_4: options_trai = options_trai + ['Trên trái xuất hiện đốm đen nhỏ sũng nước, xuất hiện nấm tạo thành một lớp màu trắng xám']
      col10.image("https://phanthuocvisinh.com/wp-content/uploads/2021/12/than-thu-sau-rieng-tren-qua.jpg", width=230, use_column_width=550)
      g_4 = col10.checkbox('Trên quả có các đốm nhỏ màu nâu hiện rõ ở hốc gai')
      if g_4: options_trai = options_trai + ['Trên quả có các đốm nhỏ màu nâu hiện rõ ở hốc gai']

   with tab5:
      col13, col14 = st.columns(2)
      col13.image("https://admin.hlc.net.vn/uploaded/Images/Original/2020/11/24/rep_sap_hai_sau_2411151001.jpg", width=230, use_column_width=550)
      b_5 = col13.checkbox('Rễ thối, xì mủ')
      if b_5: options_re = options_re + ['Rễ thối, xì mủ']
      col14.image("https://agriplusvn.com/wp-content/uploads/2020/04/IMG_20190219_060017-768x1024-min.jpg", width=230, use_column_width=550)
      c_5 = col14.checkbox('Thối rễ')
      if c_5: options_re = options_re + ['Thối rễ']

   with tab6:
      col16, col17, col18 = st.columns(3)
      col16.image("https://www.hoptri.com/images/quytrinhgiaiphap/2021/SauBenhHaiSauRieng/SauAnBongSauRieng.png", width=230, use_column_width=550)
      b_6= col16.checkbox('Bông bị hư và rụng')
      if b_6: options_hoa = options_hoa + ['Bông bị hư và rụng']
      col17.image("https://img.dantocmiennui.vn/t620/uploaddtmn//2018/6/25/sausaurieng-1.jpg", width=230, use_column_width=550)
      c_6= col17.checkbox('Cuống bông xuất hiện phân nâu đen thải ra ngoài qua lỗ đục')
      if c_6: options_hoa = options_hoa + ['Cuống bông xuất hiện phân nâu đen thải ra ngoài qua lỗ đục']
      col18.image("https://agriplusvn.com/wp-content/uploads/2020/04/89942590_2920847731310791_2863568499991642112_o.jpg", width=230, use_column_width=550)
      d_6= col18.checkbox('Cuống hoa teo tóp, hoa héo khô và rụng')
      if d_6: options_hoa = options_hoa + ['Cuống hoa teo tóp, hoa héo khô và rụng']
      col17.image("http://vidanvn.com/oamaglah/2020/12/bo-tri-sau-rieng-3.jpg", width=230, use_column_width=550)
      f_6= col17.checkbox('Cánh hoa bị thâm đen, nhụy hoa chảy nhựa')
      if f_6: options_hoa = options_hoa + ['Cánh hoa bị thâm đen, nhụy hoa chảy nhựa']
      col16.image("https://nongnghiepthuanthien.vn/wp-content/uploads/2020/10/hoa-sau-rieng-bi-than-thu.jpg", width=230, use_column_width=550)
      j_6= col16.checkbox('Trên hoa xuất hiện vết thối màu nâu xám')
      if j_6: options_hoa = options_hoa + ['Trên hoa xuất hiện vết thối màu nâu xám']

   if st.button('Chẩn đoán'):
      df = pd.read_excel('khkthpsl.xlsx')
      options_all = options_la + options_re + options_hoa \
         + options_canh + options_than + options_trai
      max = 0
      max_index = 0
      for index, case in enumerate(df.cases_of_expression.values):
         percent_case = (len(set(options_all) & set(ast.literal_eval(case))) / len(ast.literal_eval(case))*100)
         if percent_case > max: 
               max = percent_case
               
      for index, case in enumerate(df.cases_of_expression.values):
         if (len(set(options_all) & set(ast.literal_eval(case))) / len(ast.literal_eval(case))*100) == max:
               st.write('Kết quả: ',df.cases_of_diseases[index])
               st.write('Tỉ lệ dự đoán: ',round(max,2),'%')
if add_selectbox == 'Hình ảnh':
   np.set_printoptions(suppress=True)

   model = load_model('keras_model.h5', compile=False)

   class_names = open('labels.txt', 'r', encoding='utf-8').readlines()

   data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

   uploaded_file = st.file_uploader("Hãy đăng ảnh của bệnh")
   if uploaded_file is not None:
      bytes_data = uploaded_file.read()
      image_2 = Image.open(uploaded_file)
      st.image(uploaded_file)

      image = Image.open(uploaded_file).convert('RGB')

      size = (224, 224)
      image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

      image_array = np.asarray(image)

      normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

      data[0] = normalized_image_array

      prediction = model.predict(data)
      index = np.argmax(prediction)
      class_name = class_names[index]
      confidence_score = prediction[0][index]

      st.write('Bệnh rầy nhảy')
      st.write('Confidence score:', round(confidence_score*100,2),'%')
