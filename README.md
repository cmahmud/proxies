# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 408
- HTTP: 94 alive / 64 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39076
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
