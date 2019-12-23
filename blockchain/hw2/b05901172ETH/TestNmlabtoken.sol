pragma solidity >=0.4.25 <0.6.0;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Nmlabtoken.sol";

contract TestNmlabtoken {
  // Test balanceOf(account)
  function testInitialBalance() public {
    Nmlabtoken nml = Nmlabtoken(DeployedAddresses.Nmlabtoken());

    uint expected = 10000;

    Assert.equal(nml.balanceOf(msg.sender), expected, "Owner should have 10000 NML initially");
  }
  // Test totalSupply()
  function testInitialSupply() public {
    Nmlabtoken nml = Nmlabtoken(DeployedAddresses.Nmlabtoken());

    uint expected = 10000;

    Assert.equal(nml.totalSupply(), expected, "Total supply should be 10000 NML initially");
  }
  function testTransfer() public {
    // TODO
    Nmlabtoken nml = Nmlabtoken(DeployedAddresses.Nmlabtoken());

    address recipient = 0x47eD1db1B938e01006BE84403ABB18BC8c32dB6a;

    Assert.equal(nml.transfer(recipient, 0), true, "Recipient cannot be the zero address/ The caller must have a balance of at least amount") ;
  }
  function testAllowance() public {
    // TODO
    Nmlabtoken nml = Nmlabtoken(DeployedAddresses.Nmlabtoken());

    address owner = 0x47eD1db1B938e01006BE84403ABB18BC8c32dB6a;
    address spender = 0xC1bC487943DE41f51F0B015E1Fca2AdFb1bCf977;

    Assert.equal(nml.allowance(owner, spender), 0, "The remaining tokens of the for the spender will be zero at first");
  }
  function testApprove() public {
    // TODO
    Nmlabtoken nml = Nmlabtoken(DeployedAddresses.Nmlabtoken());

    address spender = 0x47eD1db1B938e01006BE84403ABB18BC8c32dB6a;

    Assert.equal(nml.approve(spender, 1000000), true, " ");

  }
  function testTransferFrom() public {
    // TODO
    Nmlabtoken nml = Nmlabtoken(DeployedAddresses.Nmlabtoken());

    address sender = 0x47eD1db1B938e01006BE84403ABB18BC8c32dB6a;
    address recipient = 0xC1bC487943DE41f51F0B015E1Fca2AdFb1bCf977;

    Assert.equal(nml.transferFrom(sender, recipient, 0), true, "");

  }
}
