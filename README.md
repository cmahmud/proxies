# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 368
- HTTP: 355 alive / 89 gold
- HTTPS: 237 alive / 27 gold
- SOCKS4: 188 alive / 120 gold
- SOCKS5: 227 alive / 132 gold

## Historical pool

- Discovered: 153747
- Ever alive: 28825
- Ever gold: 1114

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
