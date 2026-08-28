# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 423
- HTTP: 96 alive / 74 gold
- HTTPS: 115 alive / 20 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42497
- Ever gold: 1358

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
