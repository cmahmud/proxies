# SyndProxy validated proxy pool

## Current pool

- Alive now: 468
- Gold now: 391
- HTTP: 73 alive / 51 gold
- HTTPS: 45 alive / 13 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36548
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
