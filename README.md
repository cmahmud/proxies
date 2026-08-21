# SyndProxy private pool

## Current pool

- Alive now: 1178
- Gold now: 445
- HTTP: 413 alive / 106 gold
- HTTPS: 285 alive / 29 gold
- SOCKS4: 223 alive / 142 gold
- SOCKS5: 257 alive / 168 gold

## Historical pool

- Discovered: 152762
- Ever alive: 28389
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
