# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 396
- HTTP: 77 alive / 54 gold
- HTTPS: 49 alive / 15 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36611
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
