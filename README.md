# SyndProxy private pool

## Current pool

- Alive now: 961
- Gold now: 381
- HTTP: 287 alive / 93 gold
- HTTPS: 224 alive / 27 gold
- SOCKS4: 208 alive / 129 gold
- SOCKS5: 242 alive / 132 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25056
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
