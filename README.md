# SyndProxy private pool

## Current pool

- Alive now: 1068
- Gold now: 414
- HTTP: 356 alive / 96 gold
- HTTPS: 264 alive / 27 gold
- SOCKS4: 197 alive / 128 gold
- SOCKS5: 251 alive / 163 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24891
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
