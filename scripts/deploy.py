#!/usr/bin/python3
from brownie import RoadClosed
from scripts.helpful_scripts import get_account


def deploy():
    owner, _ = get_account()

    roadClosed = RoadClosed.deploy({"from": owner})
    
    print(f"Contract Deployed to {roadClosed.address}")
    return roadClosed, owner


def main():
    deploy()
