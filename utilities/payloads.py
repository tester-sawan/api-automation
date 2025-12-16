def addbook(isbn):
    payload = {
    "name":"Learn Appium Automation with Java",
    "isbn":isbn,
    "aisle":"227",
    "author":"John foe"
    }
    return payload
def deletebook(id):
    payload = {
                "ID" : id
            }
    return payload