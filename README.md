# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 405
- HTTP: 99 alive / 60 gold
- HTTPS: 55 alive / 16 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36781
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
