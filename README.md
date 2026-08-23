# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 352
- HTTP: 89 alive / 35 gold
- HTTPS: 55 alive / 10 gold
- SOCKS4: 184 alive / 151 gold
- SOCKS5: 204 alive / 156 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
