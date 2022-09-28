# cat_dog
貓狗分類器

目標：

  1.透過圖片進行學習，以CNN建立貓狗辨識的模型
  
  2.實作一個GUI，提供上傳圖檔及辨識等功能


執行環境：

    Windows 10

    訓練：Google Colab /GPU

    執行：本地 Jupyter /CPU

語言：

  Python 3.7

模型架構：

  CNN

函式庫：

    Pytorch

    tqdm

    Pandas

    Matplotlib

    Pillow


模型：

    Convolutional layer：總共4層Conv2D
  
    Pooling layer：總共4層Max Pool
  
    Fully Connected：總共4層Linear
  
    Activation Function：總共7層ReLU


經過測試：

loss的最低點約在epoch = 40左右

batch size = 32，大一點運算速度較快

learning rate = 0.01時效果較佳

  
Test Accuracy：77.4%

  
