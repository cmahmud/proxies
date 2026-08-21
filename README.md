# SyndProxy private pool

## Current pool

- Alive now: 1108
- Gold now: 426
- HTTP: 345 alive / 98 gold
- HTTPS: 254 alive / 27 gold
- SOCKS4: 238 alive / 145 gold
- SOCKS5: 271 alive / 156 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28142
- Ever gold: 1104

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
