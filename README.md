# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 436
- HTTP: 95 alive / 75 gold
- HTTPS: 77 alive / 32 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 176 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47018
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
