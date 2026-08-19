# SyndProxy private pool

## Current pool

- Alive now: 1188
- Gold now: 563
- HTTP: 440 alive / 185 gold
- HTTPS: 287 alive / 110 gold
- SOCKS4: 224 alive / 122 gold
- SOCKS5: 237 alive / 146 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19280
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
