# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 413
- HTTP: 83 alive / 58 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 189 alive / 175 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36299
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
