# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 397
- HTTP: 81 alive / 53 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 186 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36651
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
