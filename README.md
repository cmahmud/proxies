# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 394
- HTTP: 107 alive / 65 gold
- HTTPS: 78 alive / 18 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 162 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37473
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
