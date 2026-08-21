# SyndProxy private pool

## Current pool

- Alive now: 760
- Gold now: 395
- HTTP: 234 alive / 92 gold
- HTTPS: 119 alive / 20 gold
- SOCKS4: 176 alive / 124 gold
- SOCKS5: 231 alive / 159 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29483
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
