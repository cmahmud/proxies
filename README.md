# SyndProxy private pool

## Current pool

- Alive now: 1265
- Gold now: 413
- HTTP: 409 alive / 93 gold
- HTTPS: 316 alive / 20 gold
- SOCKS4: 233 alive / 141 gold
- SOCKS5: 307 alive / 159 gold

## Historical pool

- Discovered: 135761
- Ever alive: 22216
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
