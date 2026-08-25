# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 397
- HTTP: 82 alive / 54 gold
- HTTPS: 51 alive / 15 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36639
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
