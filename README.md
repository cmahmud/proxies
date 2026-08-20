# SyndProxy private pool

## Current pool

- Alive now: 1608
- Gold now: 667
- HTTP: 592 alive / 252 gold
- HTTPS: 448 alive / 129 gold
- SOCKS4: 216 alive / 127 gold
- SOCKS5: 352 alive / 159 gold

## Historical pool

- Discovered: 143489
- Ever alive: 24808
- Ever gold: 1047

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
