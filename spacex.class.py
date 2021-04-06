#%%
#!/usr/bin/env python3
"""modify the original spacex code to utilize objects of a new class"""

import requests
import crayons
from dragonclass import Dragon

# declare source of data
DATASRC="https://api.spacexdata.com/v3/dragons"

# initialize dragons list
dragons = []

def main():
    sdata = requests.get(DATASRC)

    #check request status
    if sdata.status_code == 200:       
        dragondata = sdata.json()
      
        #build dragon data from web data dictionary
        for x in dragondata: 
            dragonname = (x.get("name"))
            dragonmass = (x.get("dry_mass_kg"))
            dragonplwt = (x.get("launch_payload_mass").get("kg"))

            # add each Dragon ship into the dragons[] list, as Dragon class objects
            dragons.append(Dragon(dragonname, dragonmass, dragonplwt))
                               
        # iterate through dragons[] list and display the Dragon ship data
        for x in dragons:               
            print(f"Name: {crayons.blue(x.name)} Payload weight: {crayons.magenta(x.plwt)}", end = " ")
            if (x.mass) > 6000:
                print(f"Dry mass: {crayons.red(x.mass)} Wow! That's Heavy")                
            else:
                print(f"Dry mass: {crayons.yellow(x.mass)}")            
    else:
        print("Error with request")

if __name__ == "__main__":
    main()

