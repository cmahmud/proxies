# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 269
- HTTP: 211 alive / 28 gold
- HTTPS: 153 alive / 6 gold
- SOCKS4: 219 alive / 121 gold
- SOCKS5: 243 alive / 114 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12139
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
