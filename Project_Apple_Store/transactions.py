supportable_currencies = ["USD", "EUR", "CAD", "UAH", "GBP"]

# Currency rates for today: 03/10/2021
eur_to_usd = 1.18
cad_to_usd = 0.79
uah_to_usd = 0.03
gbp_to_usd = 1.38

usd_to_eur = 0.84
usd_to_cad = 1.26
usd_to_uah = 27.75
usd_to_gbp = 0.71
# Better to use [dict] the next time!!


class CurrencyExchange:
    def __init__(self, currency_from="USD", currency_to="USD"):
        self.currency_from = currency_from
        self.currency_to = currency_to

        # You can set your own rate but there is no reason to do it
        self.rate = None

    def convert(self, amount: int):

        # Converts from USD to something
        if self.currency_from == "USD":
            if self.currency_to == "EUR":
                self.rate = usd_to_eur
            elif self.currency_to == "CAD":
                self.rate = usd_to_cad
            elif self.currency_to == "UAH":
                self.rate = usd_to_uah
            elif self.currency_to == "GBP":
                self.rate = usd_to_gbp

        # Converts USD to something
        elif self.currency_to == "USD":
            if self.currency_from == "EUR":
                self.rate = eur_to_usd
            elif self.currency_from == "CAD":
                self.rate = cad_to_usd
            elif self.currency_from == "UAH":
                self.rate = uah_to_usd
            elif self.currency_from == "GBP":
                self.rate = gbp_to_usd
        else:
            # Converts only from and to USD. [supportable_currencies]
            return print(f"Sorry, we don't support this conversion")

        # Gives only 2 digits after the comma
        return float('{:.2f}'.format(self.rate * amount))
