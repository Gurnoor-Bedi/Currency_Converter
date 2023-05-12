import requests as r
def exchange_rate(frm,to):
  url= f"https://api.exchangerate-api.com/v4/latest/{frm}"
  response=r.get(url)
  data=response.json()
  exchangerate=data["rates"][to]
  return exchangerate
def currency_exchange(amount,frm,to):
  exchangerate=exchange_rate(frm,to)
  exchange=round(amount*exchangerate,2)
  return exchange
amount=int(input("Enter your amount"))
frm=str(input("from: "))
to=str(input("to: "))
converted_amount=currency_exchange(amount,frm,to)
print(f"{amount} {frm} = {converted_amount} {to}")