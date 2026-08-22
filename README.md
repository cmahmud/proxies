# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 390
- HTTP: 285 alive / 89 gold
- HTTPS: 159 alive / 21 gold
- SOCKS4: 203 alive / 113 gold
- SOCKS5: 250 alive / 167 gold

## Historical pool

- Discovered: 166610
- Ever alive: 32435
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
