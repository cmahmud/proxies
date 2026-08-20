# SyndProxy private pool

## Current pool

- Alive now: 1148
- Gold now: 408
- HTTP: 375 alive / 97 gold
- HTTPS: 255 alive / 20 gold
- SOCKS4: 196 alive / 128 gold
- SOCKS5: 322 alive / 163 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24863
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
