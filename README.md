# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 399
- HTTP: 89 alive / 55 gold
- HTTPS: 43 alive / 18 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36763
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
