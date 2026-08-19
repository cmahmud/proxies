# SyndProxy private pool

## Current pool

- Alive now: 996
- Gold now: 440
- HTTP: 305 alive / 122 gold
- HTTPS: 218 alive / 46 gold
- SOCKS4: 228 alive / 138 gold
- SOCKS5: 245 alive / 134 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16782
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
