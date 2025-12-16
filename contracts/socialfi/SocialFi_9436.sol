// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: SocialFi_9436
// Дата создания: 2025-12-16 08:18:30

contract SocialToken {
    mapping(address => uint256) public balances;
    mapping(address => uint256) public lastReward;
    
    string public name = "Social Reward Token";
    string public symbol = "SRT";
    uint256 public totalSupply = 1000000;
    
    event RewardClaimed(address indexed user, uint256 amount);
    
    function claimDailyReward() public {
        require(block.timestamp >= lastReward[msg.sender] + 24 hours, "Already claimed");
        
        lastReward[msg.sender] = block.timestamp;
        balances[msg.sender] += 10;
        
        emit RewardClaimed(msg.sender, 10);
    }
    
    function getBalance(address user) public view returns (uint256) {
        return balances[user];
    }
}