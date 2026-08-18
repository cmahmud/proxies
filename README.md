# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 207
- HTTP: 350 alive / 24 gold
- HTTPS: 163 alive / 9 gold
- SOCKS4: 213 alive / 96 gold
- SOCKS5: 224 alive / 78 gold

## Historical pool

- Discovered: 86776
- Ever alive: 7956
- Ever gold: 343

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
