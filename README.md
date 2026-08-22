# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 395
- HTTP: 349 alive / 86 gold
- HTTPS: 242 alive / 25 gold
- SOCKS4: 219 alive / 145 gold
- SOCKS5: 243 alive / 139 gold

## Historical pool

- Discovered: 167112
- Ever alive: 32524
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
