# GasPriceChecker

A simple get requester to the rest api of etherscan to obtain the band of gas prices.  This will provide the current block, the safe minimum / slow gap price, the average gas price, and the instant / fast gas price for the current block.  


$ Set Up

For this you will need an API key from etherscan.  
go to https://etherscan.io/register to sign up for an account.
On the profile dashboard, on the lefthand menu click on API-KEYS
near the top-center subheader, there should be a blue button  with a white addition symbol that says Add.  click this button.
Copy the code and either paste it in your project, or create an os environment for it to reside.  

Setting up URL.  To specify how you want to interact with the etherscan API, you will need to tweak the url address.  To use the Ethereum maninet use the following base: https://api.etherscan.io

To change functionality to gas tracker, add the following to the end of the base URL address: 
```?module=gastracker&action=gasoracle```

Finally you will take the API key you obtained in the set up and input it in the next part via:  &apikey={YOUR KEY GOES HERE}

This is it.  You don't need any headers, nor do you need to specify the format you want the data back in.  If you want more info, you can access the API documentation at https://docs.etherscan.io/.

The Final step is to add a CSV and paste the file path to the CSV in the main compartment of the code.  This will be an input you enter in for the update_csv function.  


I personally use cron to automate gathering gas data, however if you wanted to tweak the code to run in a forever loop, that would also be dandy.  

