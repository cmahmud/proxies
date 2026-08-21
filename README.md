# SyndProxy private pool

## Current pool

- Alive now: 1077
- Gold now: 414
- HTTP: 370 alive / 89 gold
- HTTPS: 242 alive / 21 gold
- SOCKS4: 214 alive / 146 gold
- SOCKS5: 251 alive / 158 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29510
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
