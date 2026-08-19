# SyndProxy private pool

## Current pool

- Alive now: 1111
- Gold now: 493
- HTTP: 400 alive / 119 gold
- HTTPS: 228 alive / 74 gold
- SOCKS4: 226 alive / 147 gold
- SOCKS5: 257 alive / 153 gold

## Historical pool

- Discovered: 114411
- Ever alive: 16964
- Ever gold: 627

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
