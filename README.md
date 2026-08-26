# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 375
- HTTP: 118 alive / 67 gold
- HTTPS: 63 alive / 19 gold
- SOCKS4: 150 alive / 139 gold
- SOCKS5: 170 alive / 150 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38771
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
