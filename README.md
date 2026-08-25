# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 396
- HTTP: 82 alive / 57 gold
- HTTPS: 48 alive / 12 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36509
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
