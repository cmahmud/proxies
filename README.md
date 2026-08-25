# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 396
- HTTP: 91 alive / 61 gold
- HTTPS: 81 alive / 21 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 177 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37577
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
