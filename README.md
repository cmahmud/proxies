# SyndProxy private pool

## Current pool

- Alive now: 1093
- Gold now: 438
- HTTP: 380 alive / 111 gold
- HTTPS: 237 alive / 29 gold
- SOCKS4: 224 alive / 153 gold
- SOCKS5: 252 alive / 145 gold

## Historical pool

- Discovered: 160018
- Ever alive: 30517
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
