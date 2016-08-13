# recursive-messages
Using the decorator pattern to quickly generate custom while also prewritten messages 

##Example:


%basicTemplate%, letter
>Hello %person%,
>
>%personalizedGreeting% 
>
>%spamMessage%
>
>Warmest Regards,
>%spammerName%



%spamMessage%, cats
>You should buy our nice cats~! They're only %price%


%spamMessage%, spamService
>For a limited time, we're helping you send spam for the low price of %price%!


%price%, introductoryOffer
>$15.00

%price%, wholesalePrice
>$25.00

%price%, regularPrice
>$999999999.99

##Sample actions:
* load letter
* inject %person% clueless individual
* inject cats
* inject introductoryOffer
* inject %spammerName% a random guy
* finish

##Dependencies:
* Python 3
* SQLAlchemy Library


##Sample finished message
>Hello clueless individual,
>
>You should buy our nice cats~! They're only $15.00
>
>Warmest Regards,
>a random guy

##This application is pretty useless. It's mostly just a proof of concept for a usefull possible web application (to be discussed at a future date) and also the first application I created using Vim. 
######GO TEAM VI
