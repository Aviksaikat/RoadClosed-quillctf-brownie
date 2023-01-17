# Road Closed quillctf

> Saikat Karmakar | 16 Jan 2023

## [Road Closed Link](https://quillctf.super.site/challenges/quillctf-challenges/road-closed)

# Description

“We keep out the wrong people – by letting anyone in.”

# How to Submit Solution:

Use the below submission form to submit the solution:
QuillCTF Submission Form

# Objective of CTF

Become the owner of the contract
Change the value of hacked to true

**Note**: You can create POCs using Foundry or Hardhat. Without proper POC, your submissions will not be accepted.

- Goerli link: https://goerli.etherscan.io/address/0xd2372eb76c559586be0745914e9538c17878e812

# How to solve

```bash
# run locally
# brownie compile # optional brownie run will do it anyways
brownie run scripts/attack.py

# run on goerli
brownie run scripts/attack.py main "0xD2372EB76C559586bE0745914e9538C17878E812" --network goerli
```

# POC

![](poc.png)
![](ethscanPOC.png)
