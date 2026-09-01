# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 435
- HTTP: 95 alive / 75 gold
- HTTPS: 72 alive / 31 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 176 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47018
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
