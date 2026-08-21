# SyndProxy private pool

## Current pool

- Alive now: 1121
- Gold now: 412
- HTTP: 368 alive / 97 gold
- HTTPS: 281 alive / 23 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 246 alive / 146 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28237
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
