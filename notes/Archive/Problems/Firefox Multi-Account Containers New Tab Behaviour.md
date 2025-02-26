Firefox containers are great! But the the new tab behaviour always opens new tabs in the default container. I would like new tabs to open using the container from the currently open tab.

This is not natively supported by multi-account containers, but Tree Style Tabs allows you to fix this.

Go to Tree Style Tabs Settings, turn on expert mode, and enable in "New Tabs not from Existing Tabs", Container: "Inherit from the current tab".


![[container-tab-inheritence.png]]

I found this option [on the GitHub issue for this exact problem](https://github.com/mozilla/multi-account-containers/issues/462#issuecomment-1960136802).