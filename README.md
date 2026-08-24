# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 383
- HTTP: 114 alive / 59 gold
- HTTPS: 47 alive / 9 gold
- SOCKS4: 172 alive / 155 gold
- SOCKS5: 178 alive / 160 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33441
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
