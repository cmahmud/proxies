# SyndProxy private pool

## Current pool

- Alive now: 881
- Gold now: 388
- HTTP: 270 alive / 84 gold
- HTTPS: 167 alive / 18 gold
- SOCKS4: 222 alive / 147 gold
- SOCKS5: 222 alive / 139 gold

## Historical pool

- Discovered: 155801
- Ever alive: 29398
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
