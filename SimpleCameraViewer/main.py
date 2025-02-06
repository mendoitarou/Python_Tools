import cv2

# ウェブカメラのキャプチャを開始
cap = cv2.VideoCapture(3, cv2.CAP_DSHOW)
# 自環境でobs studioにしてます。環境に合わせて数字を変更してください。

# 解像度をフルHDに設定(数値を変更することで、解像度を変えられます。)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# 解像度を出力
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# カメラの設定表示
cap.set(cv2.CAP_PROP_SETTINGS, 1)

# キャプチャがオープンしている間続ける
while(cap.isOpened()):
    # フレームを読み込む
    ret, frame = cap.read()
    if ret == True:
        # フレームを表示
        cv2.imshow('SimpleCameraViewer', frame)

        # 'q'キーが押されたらループから抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# キャプチャをリリースし、ウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
