# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 418
- HTTP: 96 alive / 67 gold
- HTTPS: 67 alive / 24 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36946
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
