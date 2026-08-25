# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 413
- HTTP: 90 alive / 67 gold
- HTTPS: 58 alive / 19 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36985
- Ever gold: 1283

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
