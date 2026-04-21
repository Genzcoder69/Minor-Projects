import qrcode as qr
upi_id = input("Enter UPI id :")

phonePay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc'
googlePay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc'

phonePay_qr = qr.make(phonePay_url)
paytm_qr = qr.make(paytm_url)
googlePay_qr = qr.make(googlePay_url)

# save the qr code to image file
phonePay_qr.save('PhonePay_qr.png')
paytm_qr.save('paytm_qr.png')
googlePay_qr.save('GooglePay.png')

phonePay_qr.show()
paytm_qr.show()
googlePay_qr.show()
