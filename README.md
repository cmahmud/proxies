# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 397
- HTTP: 106 alive / 54 gold
- HTTPS: 46 alive / 18 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 179 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36813
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
