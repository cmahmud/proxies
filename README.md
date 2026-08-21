# SyndProxy private pool

## Current pool

- Alive now: 815
- Gold now: 391
- HTTP: 239 alive / 89 gold
- HTTPS: 171 alive / 20 gold
- SOCKS4: 185 alive / 139 gold
- SOCKS5: 220 alive / 143 gold

## Historical pool

- Discovered: 152163
- Ever alive: 27853
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
