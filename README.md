# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 393
- HTTP: 108 alive / 64 gold
- HTTPS: 72 alive / 19 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 163 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37473
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
