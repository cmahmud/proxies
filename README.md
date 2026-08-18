# SyndProxy private pool

## Current pool

- Alive now: 906
- Gold now: 294
- HTTP: 286 alive / 27 gold
- HTTPS: 192 alive / 4 gold
- SOCKS4: 212 alive / 142 gold
- SOCKS5: 216 alive / 121 gold

## Historical pool

- Discovered: 102858
- Ever alive: 13502
- Ever gold: 416

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
