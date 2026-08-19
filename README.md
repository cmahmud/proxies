# SyndProxy private pool

## Current pool

- Alive now: 1156
- Gold now: 465
- HTTP: 409 alive / 122 gold
- HTTPS: 287 alive / 72 gold
- SOCKS4: 232 alive / 140 gold
- SOCKS5: 228 alive / 131 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16756
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
