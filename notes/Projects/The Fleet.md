---
subtitle: " A fleet of agents I can access from any device."
date: 2026-08-28
tags:
  - posts
---
The set up is a [[NixOS]] server with two user accounts, `~zach` and  `~agents`. The `~agents` account has a series of `pi-msg` agents. `pi-msg` is my XMPP wrapper the Pi coding harness that eschews the TUI and forces all comms to be over XMPP. Each `pi-msg` instance has name and a corresponding XMPP account.

Since its NixOS, the agents can run `nix shell -p <package>` to ephemerally install any package they desire without the need to worry about global machine state. All my projects have nix flake dev shell definitions, so the agents have exactly the correct environment for every project. Managing this without dev shells would be untenable. I do have some standard tools installed globally for them like `curl`, `gh` CLI, a mail and calendar CLI called `docket`.

The agents default directory is has a wiki about me, my projects, the infrastructure that they have access to and whatever else they think is worth committing to long term memory. They manage this, not me.

The [[Linux]] [[Unix Files#File Permissions|permission model]] is what I use to prevent the models from accessing things that they shouldn't. The agents have access to a few sysadmin scripts, such as `deploy-service` which lets them deploy a whitelisted set of services that run on `systemd` on the machine (`git pull` latest nix config to `/tmp` dir, `nix flake update <service>`, and rebuild). Since it's nix, if one of the flake updates goes wrong, the build either fails or is trivially reverted by me.  Another service is `persona-ctl` which provisions XMPP accounts and lets agents spawn/kill other agents.

![[fleet-2.png]]

Each agent know its own name as injected by `pi-msg` and one is designated the leader, though this role is more of an equal among peers. The leader's role is coordinating in group chats when agents don't take turns properly, and theoretically is in charge of spinning up other agents though all agents have access to the relevant commands. The only actual difference is that Beltino's systemd service will auto-restart. At the time of writing I have 4 long lived named agents.

On the client-side I am using the excellent Fluux, and the flawed Conversations. Fluux is made by the same team as ejabberd and clearly has great taste, though is missing some XMPP features. Conversations' XMPP functionality is great but the UI is crufty. I've forked both of these to adjust them to my taste, for example Markdown support and making the XMPP status more prominent (`pi-msg` uses that to expose the agent's current state).

The current workflow is me chatting to the named agents and telling them what to work on, or directing them to GitHub issues. For example, I have an app for [[Stash|stashing]] photos and links for later. I wanted to add JSON-LD recipe parsing to that, which is a conversation I started on my laptop, continued on my phone on the bus, where it would send me APKs over XMPP and which I would test before giving feedback.
 
Agents can be ephemeral, spawned by existing agents or by the system itself. I've set up a systemd job to watch a GitHub project set up for the fleet at a 20 minute cadence, any issues marked as "Ready" will spin up an agent called R2-D2 who will have a crack at implementing it. R2-D2 just puts up PRs that get triaged later. He can message me if he wants but there's no guarantee I will reply in time so all his context is tracked in the GitHub issue. He only takes one issue at a time, and anything outside of the GitHub issue will not be preserved. If he completes his issue, he moves it from "Ready" to "In review", if he doesn't it gets moved to "Stalled".

<div style="display:flex; gap:2rem; flex-wrap:wrap" markdown="1">

![[Screenshot_20260828-181808.png]]
![[fleet-r2d2.png]]

</div>

Having the agents with direct server access enables a lot of useful things, like debugging server specific issues. A good example of this is [[Penultimate Guitar]], where most of the routes are written to disk after first generation so they can be directly served in future. On NixOS these writes were aggressively failing because NixOS has very different expectations of what directories are writable to most operating systems. The pages still loaded within a reasonable time, so I did not notice the error until they accumulated, blew up and took down the Penultimate Guitar backend. When the site went down I was able to just ask an agent "PG went down, restart it and figure out why" on the train.  One of my agents found the problem in the error logs, read through my system config (since the whole system config is a single git repo in NixOS) and proposed a solution that worked.



NixOS and LLMs fit together very naturally. All the things that benefit humans also benefit agents, and the things that chafe humans do not chafe agents. I can tell an agent to pull a Nix flake, add it to the system config, put it behind Caddy, add Basic Auth and bam, you have a new private service.  So many things that would be an awful stateful nightmare are complete non-problems thanks to NixOS. 

I'm excited at the prospect of the agent's intelligence increasing as new models come out. Pi is model agnostic, at the time of writing all the agent are running Deepseek V4 Flash 0731, but I'll play around with others in time. Everything about this is *under construction*, but even in its young state I've gotten plenty done. I'm not someone who cares about the GitHub heat-map, but I think it illustrates that *something* has happened for me these last few weeks. 

![[fleet-heatmap.png]]

Quantity isn't quality, but it's *something*.