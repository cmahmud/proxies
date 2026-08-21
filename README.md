# SyndProxy private pool

## Current pool

- Alive now: 1144
- Gold now: 425
- HTTP: 376 alive / 98 gold
- HTTPS: 284 alive / 25 gold
- SOCKS4: 213 alive / 147 gold
- SOCKS5: 271 alive / 155 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28221
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
