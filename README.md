# SyndProxy private pool

## Current pool

- Alive now: 909
- Gold now: 280
- HTTP: 304 alive / 28 gold
- HTTPS: 120 alive / 4 gold
- SOCKS4: 247 alive / 140 gold
- SOCKS5: 238 alive / 108 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12277
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
