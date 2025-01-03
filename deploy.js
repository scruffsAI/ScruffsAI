const { ethers } = require("hardhat");

async function main() {
    const ScruffsToken = await ethers.getContractFactory("ScruffsToken");
    const scruffs = await ScruffsToken.deploy();

    console.log("ScruffsToken deployed to:", scruffs.address);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
