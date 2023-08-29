OAuth (2.0) is a standard for getting authorization to access secured resources from a third party.  For example, a *User* on my *Website* could use OAuth to connect to a Facebook *Authorization Server*, which will return a token that my *Website* can use to access *Protected Resources* through their Facebook account.

This four party model makes up the basis of OAuth: User,  Website,  Authorization Server, and Protected Resource.

Notably, no part of this flow involved giving my *Website* any personal information about the *User*.  The token that the *Authorization Server* returns is not depedent on the *Website*, so any other application/site that implements OAuth with Facebook would be able to issue a token that is equally valid for use to access *Protected Resources* through my website if they injected into my *Website.  **For this reason, OAuth alone should not be used for authentication, only authorization.**

More on this can be read in an [excellent article by John Bradley](http://www.thread-safe.com/2012/01/problem-with-oauth-for-authentication.html).  A few more thoughts on this can be read in this [StackExchange thread](https://security.stackexchange.com/questions/37818/why-use-openid-connect-instead-of-plain-oauth2/260519#260519).

Authentication should be handled by OpenID Connect, which provides an identity layer on top of OAuth 2.0.