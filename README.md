# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 394
- HTTP: 84 alive / 53 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 174 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36763
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
