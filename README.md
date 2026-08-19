# SyndProxy private pool

## Current pool

- Alive now: 1094
- Gold now: 536
- HTTP: 387 alive / 160 gold
- HTTPS: 276 alive / 90 gold
- SOCKS4: 222 alive / 155 gold
- SOCKS5: 209 alive / 131 gold

## Historical pool

- Discovered: 119828
- Ever alive: 18210
- Ever gold: 716

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
