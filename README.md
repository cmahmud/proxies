# SyndProxy private pool

## Current pool

- Alive now: 927
- Gold now: 347
- HTTP: 294 alive / 51 gold
- HTTPS: 186 alive / 12 gold
- SOCKS4: 216 alive / 133 gold
- SOCKS5: 231 alive / 151 gold

## Historical pool

- Discovered: 107131
- Ever alive: 14910
- Ever gold: 478

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
