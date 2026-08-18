# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 305
- HTTP: 369 alive / 31 gold
- HTTPS: 212 alive / 4 gold
- SOCKS4: 219 alive / 143 gold
- SOCKS5: 212 alive / 127 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13440
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
