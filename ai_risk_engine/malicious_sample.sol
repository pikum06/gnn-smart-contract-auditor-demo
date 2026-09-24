pragma solidity ^0.8.0;

contract HighYieldVault {
    address public owner;
    mapping(address => uint) public balances;
    
    constructor() {
        owner = msg.sender;
    }

    // RED FLAG: A "mint" style function that lets the owner create tokens
    function emergencyMint(uint amount) public {
        require(msg.sender == owner, "Not owner");
        balances[owner] += amount;
    }

    // RED FLAG: Allows owner to kill the contract and take all funds
    function closeVault() public {
        require(msg.sender == owner);
        selfdestruct(payable(owner));
    }
}