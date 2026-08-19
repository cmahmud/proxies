# SyndProxy private pool

## Current pool

- Alive now: 1272
- Gold now: 413
- HTTP: 408 alive / 94 gold
- HTTPS: 329 alive / 20 gold
- SOCKS4: 234 alive / 141 gold
- SOCKS5: 301 alive / 158 gold

## Historical pool

- Discovered: 135761
- Ever alive: 22210
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
