# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 398
- HTTP: 96 alive / 63 gold
- HTTPS: 62 alive / 17 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 185 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38707
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
