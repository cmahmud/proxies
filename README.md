# SyndProxy private pool

## Current pool

- Alive now: 877
- Gold now: 261
- HTTP: 273 alive / 29 gold
- HTTPS: 160 alive / 3 gold
- SOCKS4: 223 alive / 120 gold
- SOCKS5: 221 alive / 109 gold

## Historical pool

- Discovered: 99145
- Ever alive: 12065
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
