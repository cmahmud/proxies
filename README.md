# SyndProxy private pool

## Current pool

- Alive now: 1078
- Gold now: 414
- HTTP: 346 alive / 98 gold
- HTTPS: 250 alive / 24 gold
- SOCKS4: 192 alive / 127 gold
- SOCKS5: 290 alive / 165 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24881
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
