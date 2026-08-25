# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 388
- HTTP: 76 alive / 51 gold
- HTTPS: 45 alive / 12 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36544
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
