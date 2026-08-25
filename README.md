# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 397
- HTTP: 95 alive / 54 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36831
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
