# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 402
- HTTP: 91 alive / 59 gold
- HTTPS: 66 alive / 17 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38495
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
