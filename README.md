# SyndProxy private pool

## Current pool

- Alive now: 942
- Gold now: 324
- HTTP: 287 alive / 36 gold
- HTTPS: 197 alive / 10 gold
- SOCKS4: 230 alive / 147 gold
- SOCKS5: 228 alive / 131 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14205
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
