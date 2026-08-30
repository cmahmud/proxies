# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 436
- HTTP: 119 alive / 83 gold
- HTTPS: 56 alive / 24 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 202 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44550
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
