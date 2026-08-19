# SyndProxy private pool

## Current pool

- Alive now: 1101
- Gold now: 366
- HTTP: 376 alive / 74 gold
- HTTPS: 257 alive / 13 gold
- SOCKS4: 213 alive / 126 gold
- SOCKS5: 255 alive / 153 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20371
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
