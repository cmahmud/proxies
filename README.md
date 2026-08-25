# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 413
- HTTP: 103 alive / 71 gold
- HTTPS: 68 alive / 17 gold
- SOCKS4: 167 alive / 158 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34827
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
