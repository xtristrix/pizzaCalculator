// Copyright (c) 2017, Tristan Eberhart
// Use of this source code is governed by the
// GNU General Public License Version 2
// which can be found in the LICENSE file.

import calculation
import questions

print ("First enter the informations about the small pizza.")

diameterSmall = calculation.area(questions.diameter())
priceSmall = questions.price()
smallSquareCMPrice = calculation.pricePerSquareCM(priceSmall, diameterSmall)

print ("The price for a small pizza per cm² is", round(smallSquareCMPrice, 5),"€.")


print ("Please enter the informations about the large pizza:")

diameterLarge = calculation.area(questions.diameter())
priceLarge = questions.price()
largeSquareCMPrice = calculation.pricePerSquareCM(priceLarge, diameterLarge)


print ("The price for a small pizza per cm² is", round(largeSquareCMPrice, 5),"€.")

if largeSquareCMPrice > smallSquareCMPrice:
    print ("The large one is more expansive. Two smaller ones are cheaper.")
elif smallSquareCMPrice > largeSquareCMPrice:
    print ("The large one is cheaper. I would prefer to buy this one.")
else:
    print ("The prices are exactly the same per cm². Buy whatever you want.")

if smallSquareCMPrice > largeSquareCMPrice:
    print ("The difference between the large and the small one is", round(smallSquareCMPrice - largeSquareCMPrice, 5), "€ per cm².")
elif largeSquareCMPrice > smallSquareCMPrice:
    print ("The difference between the large and the small one is", round(largeSquareCMPrice - smallSquareCMPrice, 5), "€ per cm².")
else:
    print ("There is no difference at the price.")