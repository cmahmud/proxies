# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 391
- HTTP: 86 alive / 61 gold
- HTTPS: 74 alive / 18 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 166 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37541
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
