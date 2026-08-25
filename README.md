# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 391
- HTTP: 105 alive / 65 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 160 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37492
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
