# SyndProxy private pool

## Current pool

- Alive now: 1096
- Gold now: 287
- HTTP: 364 alive / 30 gold
- HTTPS: 239 alive / 4 gold
- SOCKS4: 245 alive / 137 gold
- SOCKS5: 248 alive / 116 gold

## Historical pool

- Discovered: 100167
- Ever alive: 12662
- Ever gold: 398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
