# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 269
- HTTP: 211 alive / 28 gold
- HTTPS: 138 alive / 5 gold
- SOCKS4: 236 alive / 120 gold
- SOCKS5: 238 alive / 116 gold

## Historical pool

- Discovered: 99165
- Ever alive: 12140
- Ever gold: 395

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
