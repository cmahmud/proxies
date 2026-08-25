# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 413
- HTTP: 93 alive / 63 gold
- HTTPS: 59 alive / 22 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36939
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
