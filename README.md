# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 384
- HTTP: 246 alive / 76 gold
- HTTPS: 150 alive / 22 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 212 alive / 145 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25264
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
