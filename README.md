# SyndProxy private pool

## Current pool

- Alive now: 935
- Gold now: 324
- HTTP: 279 alive / 35 gold
- HTTPS: 191 alive / 10 gold
- SOCKS4: 237 alive / 147 gold
- SOCKS5: 228 alive / 132 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14205
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
