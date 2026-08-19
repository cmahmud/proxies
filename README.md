# SyndProxy private pool

## Current pool

- Alive now: 1131
- Gold now: 391
- HTTP: 375 alive / 87 gold
- HTTPS: 290 alive / 14 gold
- SOCKS4: 214 alive / 127 gold
- SOCKS5: 252 alive / 163 gold

## Historical pool

- Discovered: 131855
- Ever alive: 21285
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
