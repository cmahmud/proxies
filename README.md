# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 280
- HTTP: 309 alive / 27 gold
- HTTPS: 140 alive / 4 gold
- SOCKS4: 236 alive / 140 gold
- SOCKS5: 244 alive / 109 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12311
- Ever gold: 396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
