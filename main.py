while True:
    given_date = input("Date: ")
    date_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    date = given_date.split("/")
    date_words = given_date.split(" ")

    if date_words[0] in date_dict:

        if "," in date_words[1] and int(date_words[1].replace(",", "")) < 32:
            break
    else:
        if int(date[0]) < 13 and int(date[1]) < 32:
            break


if date_words[0] in date_dict:
    month = date_words[0]
    month = date_dict[month]
    month = str(month).rjust(2, '0')

    date_words[1] = date_words[1].replace(",", "")
    date_words[1] = str(date_words[1]).rjust(2, "0")

    formatted_date = date_words[2] + "-" + month + "-" + date_words[1]
    print(formatted_date)

else:
    date[0] = date[0].rjust(2, '0')
    date[1] = date[1].rjust(2, '0')

    formatted_date = date[2] + "-" + date[0] + "-" + date[1]
    print(str(formatted_date))
