# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 382
- HTTP: 106 alive / 54 gold
- HTTPS: 41 alive / 11 gold
- SOCKS4: 172 alive / 157 gold
- SOCKS5: 180 alive / 160 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33444
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
