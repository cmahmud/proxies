# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 413
- HTTP: 262 alive / 90 gold
- HTTPS: 156 alive / 25 gold
- SOCKS4: 238 alive / 152 gold
- SOCKS5: 225 alive / 146 gold

## Historical pool

- Discovered: 166322
- Ever alive: 32385
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
