# SyndProxy private pool

## Current pool

- Alive now: 880
- Gold now: 285
- HTTP: 259 alive / 25 gold
- HTTPS: 161 alive / 4 gold
- SOCKS4: 227 alive / 143 gold
- SOCKS5: 233 alive / 113 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12336
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
