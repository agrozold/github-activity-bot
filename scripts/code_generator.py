import os
import random
import datetime

# Простые шаблоны контрактов
SOCIALFI_CONTRACTS = [
    '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: {}
// Дата создания: {}

contract SocialProfile {{
    struct Profile {{
        string username;
        string bio;
        uint256 reputation;
        bool verified;
    }}
    
    mapping(address => Profile) public profiles;
    
    event ProfileCreated(address indexed user, string username);
    
    function createProfile(string memory _username, string memory _bio) public {{
        profiles[msg.sender] = Profile(_username, _bio, 100, false);
        emit ProfileCreated(msg.sender, _username);
    }}
    
    function getProfile(address user) public view returns (Profile memory) {{
        return profiles[user];
    }}
}}''',

    '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: {}
// Дата создания: {}

contract SocialToken {{
    mapping(address => uint256) public balances;
    mapping(address => uint256) public lastReward;
    
    string public name = "Social Reward Token";
    string public symbol = "SRT";
    uint256 public totalSupply = 1000000;
    
    event RewardClaimed(address indexed user, uint256 amount);
    
    function claimDailyReward() public {{
        require(block.timestamp >= lastReward[msg.sender] + 24 hours, "Already claimed");
        
        lastReward[msg.sender] = block.timestamp;
        balances[msg.sender] += 10;
        
        emit RewardClaimed(msg.sender, 10);
    }}
    
    function getBalance(address user) public view returns (uint256) {{
        return balances[user];
    }}
}}'''
]

DEFI_CONTRACTS = [
    '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: {}
// Дата создания: {}

contract SimpleDEX {{
    mapping(address => uint256) public ethBalance;
    mapping(address => uint256) public tokenBalance;
    
    uint256 public ethReserve;
    uint256 public tokenReserve;
    
    event LiquidityAdded(address indexed provider, uint256 ethAmount, uint256 tokenAmount);
    event TokensSwapped(address indexed user, uint256 ethIn, uint256 tokensOut);
    
    function addLiquidity(uint256 tokenAmount) public payable {{
        ethReserve += msg.value;
        tokenReserve += tokenAmount;
        
        ethBalance[msg.sender] += msg.value;
        tokenBalance[msg.sender] += tokenAmount;
        
        emit LiquidityAdded(msg.sender, msg.value, tokenAmount);
    }}
    
    function swapEthForTokens() public payable {{
        uint256 tokensOut = (msg.value * tokenReserve) / ethReserve;
        ethReserve += msg.value;
        tokenReserve -= tokensOut;
        
        emit TokensSwapped(msg.sender, msg.value, tokensOut);
    }}
}}''',

    '''// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Автоматически сгенерированный контракт: {}
// Дата создания: {}

contract StakingPool {{
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public stakeTime;
    mapping(address => uint256) public rewards;
    
    uint256 public totalStaked;
    uint256 public rewardRate = 10; // 10% годовых
    
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);
    
    function stake() public payable {{
        require(msg.value > 0, "Must stake something");
        
        stakedAmount[msg.sender] += msg.value;
        stakeTime[msg.sender] = block.timestamp;
        totalStaked += msg.value;
        
        emit Staked(msg.sender, msg.value);
    }}
    
    function calculateReward(address user) public view returns (uint256) {{
        if (stakedAmount[user] == 0) return 0;
        
        uint256 timeStaked = block.timestamp - stakeTime[user];
        uint256 reward = (stakedAmount[user] * rewardRate * timeStaked) / (365 days * 100);
        
        return reward;
    }}
    
    function withdraw() public {{
        uint256 amount = stakedAmount[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        
        require(amount > 0, "Nothing to withdraw");
        
        stakedAmount[msg.sender] = 0;
        totalStaked -= amount;
        
        payable(msg.sender).transfer(amount + reward);
        emit Withdrawn(msg.sender, amount, reward);
    }}
}}'''
]

def generate_contract():
    """Генерирует случайный контракт"""
    contract_type = random.choice(["socialfi", "defi"])
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    if contract_type == "socialfi":
        template = random.choice(SOCIALFI_CONTRACTS)
        contract_name = f"SocialFi_{random.randint(1000, 9999)}"
    else:
        template = random.choice(DEFI_CONTRACTS)
        contract_name = f"DeFi_{random.randint(1000, 9999)}"
    
    # Заполняем шаблон
    contract_code = template.format(contract_name, timestamp)
    
    return contract_type, contract_name, contract_code

def save_contract(contract_type, contract_name, contract_code):
    """Сохраняет контракт в файл"""
    # Создаем папку если не существует
    folder = f"contracts/{contract_type}"
    os.makedirs(folder, exist_ok=True)
    
    # Имя файла
    filename = f"{folder}/{contract_name}.sol"
    
    # Сохраняем файл
    with open(filename, "w", encoding="utf-8") as f:
        f.write(contract_code)
    
    return filename

def update_readme(contract_type, contract_name):
    """Обновляет README.md"""
    readme_content = f"""# 🤖 GitHub Activity Bot

Этот репозиторий автоматически генерирует Smart Contracts для изучения блокчейн разработки.

## 📊 Статистика

**Последнее обновление:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Последний контракт:** {contract_name} ({contract_type.upper()})

## 📁 Структура

- `contracts/defi/` - DeFi контракты (DEX, стейкинг, фарминг)
- `contracts/socialfi/` - Social-Fi контракты (профили, токены, репутация)
- `scripts/` - Скрипты автоматизации

## 🎯 Цель проекта

Изучение и практика создания Smart Contracts в области:
- **DeFi** (Децентрализованные финансы)
- **Social-Fi** (Социальные финансы)

## ⚡ Автоматизация

Контракты генерируются автоматически через GitHub Actions каждые несколько часов.

---
*Создано с помощью GitHub Activity Bot 🚀*
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

def main():
    """Основная функция"""
    print("🚀 Генерируем новый контракт...")
    
    # Генерируем контракт
    contract_type, contract_name, contract_code = generate_contract()
    
    # Сохраняем файл
    filename = save_contract(contract_type, contract_name, contract_code)
    
    # Обновляем README
    update_readme(contract_type, contract_name)
    
    print(f"✅ Создан контракт: {filename}")
    print(f"📝 Тип: {contract_type.upper()}")
    print(f"🏷️ Название: {contract_name}")

if __name__ == "__main__":
    main()
