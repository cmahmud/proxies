# SyndProxy private pool

## Current pool

- Alive now: 1064
- Gold now: 405
- HTTP: 361 alive / 110 gold
- HTTPS: 260 alive / 24 gold
- SOCKS4: 223 alive / 149 gold
- SOCKS5: 220 alive / 122 gold

## Historical pool

- Discovered: 153722
- Ever alive: 28544
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
