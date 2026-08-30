# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 431
- HTTP: 98 alive / 78 gold
- HTTPS: 51 alive / 24 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 204 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44554
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
