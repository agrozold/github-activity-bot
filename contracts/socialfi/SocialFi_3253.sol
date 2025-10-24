// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: SocialFi_3253
// Дата создания: 2025-10-24 12:22:54

contract SocialProfile {
    struct Profile {
        string username;
        string bio;
        uint256 reputation;
        bool verified;
    }
    
    mapping(address => Profile) public profiles;
    
    event ProfileCreated(address indexed user, string username);
    
    function createProfile(string memory _username, string memory _bio) public {
        profiles[msg.sender] = Profile(_username, _bio, 100, false);
        emit ProfileCreated(msg.sender, _username);
    }
    
    function getProfile(address user) public view returns (Profile memory) {
        return profiles[user];
    }
}