# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 398
- HTTP: 234 alive / 87 gold
- HTTPS: 145 alive / 22 gold
- SOCKS4: 192 alive / 133 gold
- SOCKS5: 233 alive / 156 gold

## Historical pool

- Discovered: 151681
- Ever alive: 27679
- Ever gold: 1102

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
