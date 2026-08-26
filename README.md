# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 407
- HTTP: 112 alive / 63 gold
- HTTPS: 84 alive / 17 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38363
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
