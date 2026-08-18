# SyndProxy private pool

## Current pool

- Alive now: 857
- Gold now: 265
- HTTP: 226 alive / 29 gold
- HTTPS: 169 alive / 4 gold
- SOCKS4: 216 alive / 120 gold
- SOCKS5: 246 alive / 112 gold

## Historical pool

- Discovered: 99162
- Ever alive: 12138
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
