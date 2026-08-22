# SyndProxy private pool

## Current pool

- Alive now: 876
- Gold now: 413
- HTTP: 268 alive / 87 gold
- HTTPS: 141 alive / 28 gold
- SOCKS4: 237 alive / 151 gold
- SOCKS5: 230 alive / 147 gold

## Historical pool

- Discovered: 166318
- Ever alive: 32382
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
