# SyndProxy private pool

## Current pool

- Alive now: 1115
- Gold now: 415
- HTTP: 359 alive / 100 gold
- HTTPS: 244 alive / 23 gold
- SOCKS4: 195 alive / 128 gold
- SOCKS5: 317 alive / 164 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24873
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
