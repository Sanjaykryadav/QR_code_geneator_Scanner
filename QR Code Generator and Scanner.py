#importing required modules

import qrcode
import cv2
import webbrowser

inp = int(input("Enter your choice : \n 1) Generate QR Code \n 2) Scan a QR Code \t:  "))

if (inp == 1):
    
    #taking required url input
    url = input("Enter link : ")

    input_URL = url

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4,
        )

    qr.add_data(input_URL)
    qr.make(fit=True)
    
    #Customize QR 
        
    f_color=input("Choose Fill Color : ")
    b_color=input("Choose Back Color : ")
    
    #saving QRCode 
    
    img = qr.make_image(fill_color=f_color, back_color=b_color)
    img.save("QR.png")

    #Result
    
    print(qr.data_list)

elif (inp == 2):
        
    # initalize the camera
    
    cap = cv2.VideoCapture(0)
        
    # initialize the cv2 QRCode detector
    
    detector = cv2.QRCodeDetector()
        
    while True:
        _, img = cap.read()
            
        # detect and decode img
        
        data, bbox, _ = detector.detectAndDecode(img)
            
        # check if there is a QRCode in the image
        
        if data:
            a = data
            break
            
        # display the result
        
        cv2.imshow("QRCODEscanner", img)
        if cv2.waitKey(1) == ord("q"):
            break

    b = webbrowser.open(str(a))
    cap.release()
    cv2.destroyAllWindows()

