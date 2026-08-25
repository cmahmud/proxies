# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 396
- HTTP: 99 alive / 63 gold
- HTTPS: 73 alive / 20 gold
- SOCKS4: 163 alive / 157 gold
- SOCKS5: 170 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37239
- Ever gold: 1284

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
