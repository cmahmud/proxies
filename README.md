# SyndProxy validated proxy pool

## Current pool

- Alive now: 476
- Gold now: 397
- HTTP: 76 alive / 56 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 180 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36532
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
