Status Messenger is an extension for VS Code (and [VSCodium](https://vscodium.com/)) that places a message in the editor status bar that is periodically updated by a remote server.  This was built so that I could shame people at work with a counter that said how many days its been since somebody broke a prod deployment.

![[status-messenger-1.png]]

On install, the user will be prompted to enter a URL.  This URL should be an API that responds with a message with the following schema:
```ts
{ [title: string]: string}
```

An example of a return value is:
```json
{
	"DEV":"0 days since last broken DEV deployment",
	"PROD":"PROD has never had a broken deployment",
	"UAT":"90 days since last broken UAT deployment"
}
```

This URL can be changed using the **Set Remote Message URL** command.

![[status-messenger-3.png]]

Each key corresponds to a different message variant that will display in the status bar. These can be switched between using the **Set Message Variant** command, or by clicking on the message in the status bar.

![[status-messenger-2.png]]

The extension will automatically pull messages from the server every 20 minutes after opening VS Code.  It will stop displaying and updating the message if the **Hide Status Bar Message** command is used.  It can be brought back using the **Set Status Message Variant**.

The URL and variant is stored per workspace, so different workspaces can have different servers or variants.

The extension is built with TypeScript and is available on [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ZachManson.status-messenger) and [Open VSX](https://open-vsx.org/extension/ZachManson/status-messenger).  The source code is available on [GitHub](https://github.com/pavo-etc/status-messenger).