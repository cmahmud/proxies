# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 388
- HTTP: 109 alive / 66 gold
- HTTPS: 88 alive / 17 gold
- SOCKS4: 167 alive / 150 gold
- SOCKS5: 178 alive / 155 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39327
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
