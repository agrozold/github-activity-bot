// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: DeFi_8912
// Дата создания: 2026-01-05 01:05:31

contract SimpleDEX {
    mapping(address => uint256) public ethBalance;
    mapping(address => uint256) public tokenBalance;
    
    uint256 public ethReserve;
    uint256 public tokenReserve;
    
    event LiquidityAdded(address indexed provider, uint256 ethAmount, uint256 tokenAmount);
    event TokensSwapped(address indexed user, uint256 ethIn, uint256 tokensOut);
    
    function addLiquidity(uint256 tokenAmount) public payable {
        ethReserve += msg.value;
        tokenReserve += tokenAmount;
        
        ethBalance[msg.sender] += msg.value;
        tokenBalance[msg.sender] += tokenAmount;
        
        emit LiquidityAdded(msg.sender, msg.value, tokenAmount);
    }
    
    function swapEthForTokens() public payable {
        uint256 tokensOut = (msg.value * tokenReserve) / ethReserve;
        ethReserve += msg.value;
        tokenReserve -= tokensOut;
        
        emit TokensSwapped(msg.sender, msg.value, tokensOut);
    }
}