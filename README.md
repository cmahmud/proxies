# SyndProxy validated proxy pool

## Current pool

- Alive now: 655
- Gold now: 450
- HTTP: 125 alive / 87 gold
- HTTPS: 137 alive / 31 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 219 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46612
- Ever gold: 1445

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
