# SyndProxy private pool

## Current pool

- Alive now: 1070
- Gold now: 395
- HTTP: 393 alive / 103 gold
- HTTPS: 216 alive / 23 gold
- SOCKS4: 227 alive / 131 gold
- SOCKS5: 234 alive / 138 gold

## Historical pool

- Discovered: 160027
- Ever alive: 30606
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
