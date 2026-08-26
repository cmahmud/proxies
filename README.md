# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 370
- HTTP: 100 alive / 63 gold
- HTTPS: 66 alive / 14 gold
- SOCKS4: 152 alive / 143 gold
- SOCKS5: 178 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38810
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
