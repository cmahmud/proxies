# SyndProxy private pool

## Current pool

- Alive now: 721
- Gold now: 367
- HTTP: 177 alive / 73 gold
- HTTPS: 141 alive / 16 gold
- SOCKS4: 179 alive / 118 gold
- SOCKS5: 224 alive / 160 gold

## Historical pool

- Discovered: 148333
- Ever alive: 26124
- Ever gold: 1079

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
