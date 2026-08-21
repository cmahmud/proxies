# SyndProxy private pool

## Current pool

- Alive now: 928
- Gold now: 405
- HTTP: 287 alive / 96 gold
- HTTPS: 209 alive / 28 gold
- SOCKS4: 227 alive / 155 gold
- SOCKS5: 205 alive / 126 gold

## Historical pool

- Discovered: 160987
- Ever alive: 30863
- Ever gold: 1150

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
