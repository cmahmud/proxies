# SyndProxy validated proxy pool

## Current pool

- Alive now: 458
- Gold now: 394
- HTTP: 83 alive / 56 gold
- HTTPS: 36 alive / 16 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 174 alive / 162 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36767
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
