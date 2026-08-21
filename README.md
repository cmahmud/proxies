# SyndProxy private pool

## Current pool

- Alive now: 804
- Gold now: 390
- HTTP: 237 alive / 89 gold
- HTTPS: 165 alive / 20 gold
- SOCKS4: 182 alive / 138 gold
- SOCKS5: 220 alive / 143 gold

## Historical pool

- Discovered: 152163
- Ever alive: 27855
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
