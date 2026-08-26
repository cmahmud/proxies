# SyndProxy validated proxy pool

## Current pool

- Alive now: 570
- Gold now: 408
- HTTP: 98 alive / 63 gold
- HTTPS: 84 alive / 13 gold
- SOCKS4: 187 alive / 162 gold
- SOCKS5: 201 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38161
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
