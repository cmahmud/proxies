# SyndProxy private pool

## Current pool

- Alive now: 979
- Gold now: 355
- HTTP: 281 alive / 65 gold
- HTTPS: 243 alive / 14 gold
- SOCKS4: 231 alive / 126 gold
- SOCKS5: 224 alive / 150 gold

## Historical pool

- Discovered: 129286
- Ever alive: 20269
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
