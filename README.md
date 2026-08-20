# SyndProxy private pool

## Current pool

- Alive now: 793
- Gold now: 363
- HTTP: 213 alive / 71 gold
- HTTPS: 164 alive / 18 gold
- SOCKS4: 201 alive / 133 gold
- SOCKS5: 215 alive / 141 gold

## Historical pool

- Discovered: 149501
- Ever alive: 26707
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
