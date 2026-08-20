# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 416
- HTTP: 364 alive / 99 gold
- HTTPS: 254 alive / 27 gold
- SOCKS4: 195 alive / 127 gold
- SOCKS5: 271 alive / 163 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24881
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
