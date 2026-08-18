# SyndProxy private pool

## Current pool

- Alive now: 1162
- Gold now: 286
- HTTP: 472 alive / 27 gold
- HTTPS: 222 alive / 7 gold
- SOCKS4: 231 alive / 130 gold
- SOCKS5: 237 alive / 122 gold

## Historical pool

- Discovered: 102839
- Ever alive: 13121
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
