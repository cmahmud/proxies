# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 397
- HTTP: 83 alive / 57 gold
- HTTPS: 42 alive / 12 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 177 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36509
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
