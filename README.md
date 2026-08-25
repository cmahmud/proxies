# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 397
- HTTP: 73 alive / 50 gold
- HTTPS: 55 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 187 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36568
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
