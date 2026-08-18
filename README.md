# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 258
- HTTP: 431 alive / 31 gold
- HTTPS: 185 alive / 4 gold
- SOCKS4: 238 alive / 117 gold
- SOCKS5: 240 alive / 106 gold

## Historical pool

- Discovered: 95405
- Ever alive: 11000
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
