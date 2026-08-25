# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 397
- HTTP: 95 alive / 54 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 183 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36830
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
