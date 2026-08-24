# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 381
- HTTP: 107 alive / 54 gold
- HTTPS: 34 alive / 11 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33444
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
