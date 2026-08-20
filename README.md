# SyndProxy private pool

## Current pool

- Alive now: 664
- Gold now: 352
- HTTP: 176 alive / 68 gold
- HTTPS: 107 alive / 18 gold
- SOCKS4: 186 alive / 126 gold
- SOCKS5: 195 alive / 140 gold

## Historical pool

- Discovered: 145577
- Ever alive: 25572
- Ever gold: 1066

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
