# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 349
- HTTP: 143 alive / 39 gold
- HTTPS: 64 alive / 10 gold
- SOCKS4: 170 alive / 152 gold
- SOCKS5: 176 alive / 148 gold

## Historical pool

- Discovered: 171044
- Ever alive: 32847
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
