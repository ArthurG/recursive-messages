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
>load letter
>inject %person% clueless individual
>inject cats
>inject introductoryOffer
>inject %spammerName% a random guy
>finish

##Sample finished message
>Hello clueless individual,
>
>You should buy our nice cats~! They're only $15.00
>
>Warmest Regards,
>a random guy
