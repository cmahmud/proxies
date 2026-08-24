# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 432
- HTTP: 122 alive / 79 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34017
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
