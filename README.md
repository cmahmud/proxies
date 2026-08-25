# SyndProxy validated proxy pool

## Current pool

- Alive now: 474
- Gold now: 399
- HTTP: 86 alive / 59 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36757
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
