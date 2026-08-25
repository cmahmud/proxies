# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 399
- HTTP: 77 alive / 57 gold
- HTTPS: 39 alive / 13 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 179 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36511
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
