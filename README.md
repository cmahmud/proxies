# SyndProxy private pool

## Current pool

- Alive now: 682
- Gold now: 255
- HTTP: 185 alive / 33 gold
- HTTPS: 96 alive / 8 gold
- SOCKS4: 189 alive / 112 gold
- SOCKS5: 212 alive / 102 gold

## Historical pool

- Discovered: 95381
- Ever alive: 10238
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
