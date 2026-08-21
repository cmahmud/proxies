# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 405
- HTTP: 257 alive / 89 gold
- HTTPS: 197 alive / 22 gold
- SOCKS4: 228 alive / 146 gold
- SOCKS5: 243 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29095
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
