# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 309
- HTTP: 293 alive / 37 gold
- HTTPS: 195 alive / 9 gold
- SOCKS4: 228 alive / 138 gold
- SOCKS5: 221 alive / 125 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14205
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
