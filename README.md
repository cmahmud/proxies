# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 383
- HTTP: 89 alive / 57 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 180 alive / 156 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33111
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
