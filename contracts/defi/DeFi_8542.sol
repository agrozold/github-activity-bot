// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: DeFi_8542
// Дата создания: 2025-10-30 04:13:36

contract StakingPool {
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public stakeTime;
    mapping(address => uint256) public rewards;
    
    uint256 public totalStaked;
    uint256 public rewardRate = 10; // 10% годовых
    
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);
    
    function stake() public payable {
        require(msg.value > 0, "Must stake something");
        
        stakedAmount[msg.sender] += msg.value;
        stakeTime[msg.sender] = block.timestamp;
        totalStaked += msg.value;
        
        emit Staked(msg.sender, msg.value);
    }
    
    function calculateReward(address user) public view returns (uint256) {
        if (stakedAmount[user] == 0) return 0;
        
        uint256 timeStaked = block.timestamp - stakeTime[user];
        uint256 reward = (stakedAmount[user] * rewardRate * timeStaked) / (365 days * 100);
        
        return reward;
    }
    
    function withdraw() public {
        uint256 amount = stakedAmount[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        
        require(amount > 0, "Nothing to withdraw");
        
        stakedAmount[msg.sender] = 0;
        totalStaked -= amount;
        
        payable(msg.sender).transfer(amount + reward);
        emit Withdrawn(msg.sender, amount, reward);
    }
}