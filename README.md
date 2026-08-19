# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 341
- HTTP: 343 alive / 61 gold
- HTTPS: 212 alive / 17 gold
- SOCKS4: 209 alive / 131 gold
- SOCKS5: 207 alive / 132 gold

## Historical pool

- Discovered: 129235
- Ever alive: 20046
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
