# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 407
- HTTP: 114 alive / 63 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 187 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38362
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
