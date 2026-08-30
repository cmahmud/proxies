# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 432
- HTTP: 110 alive / 81 gold
- HTTPS: 46 alive / 23 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44519
- Ever gold: 1403

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
