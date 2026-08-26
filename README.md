# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 408
- HTTP: 102 alive / 61 gold
- HTTPS: 55 alive / 17 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38302
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
