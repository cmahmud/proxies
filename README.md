# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 532
- HTTP: 312 alive / 159 gold
- HTTPS: 259 alive / 87 gold
- SOCKS4: 235 alive / 154 gold
- SOCKS5: 201 alive / 132 gold

## Historical pool

- Discovered: 119814
- Ever alive: 18126
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
