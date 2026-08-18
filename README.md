# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 290
- HTTP: 286 alive / 26 gold
- HTTPS: 164 alive / 4 gold
- SOCKS4: 222 alive / 143 gold
- SOCKS5: 224 alive / 117 gold

## Historical pool

- Discovered: 102812
- Ever alive: 12775
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
