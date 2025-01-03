// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title ScruffsToken
/// @notice A secure token leveraging ai16z-inspired frameworks for AI-driven monitoring.
contract ScruffsToken {
    string public name = "Scruffs Token";
    string public symbol = "SCRUFFS";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals));

    constructor() {
        // Mint initial supply to contract creator
        balances[msg.sender] = totalSupply;
    }
}
