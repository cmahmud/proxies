# SyndProxy private pool

## Current pool

- Alive now: 1074
- Gold now: 416
- HTTP: 360 alive / 98 gold
- HTTPS: 250 alive / 27 gold
- SOCKS4: 199 alive / 128 gold
- SOCKS5: 265 alive / 163 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24882
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
