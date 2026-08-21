# SyndProxy private pool

## Current pool

- Alive now: 811
- Gold now: 388
- HTTP: 249 alive / 84 gold
- HTTPS: 116 alive / 16 gold
- SOCKS4: 209 alive / 136 gold
- SOCKS5: 237 alive / 152 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29752
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
