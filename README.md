# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 351
- HTTP: 281 alive / 65 gold
- HTTPS: 258 alive / 19 gold
- SOCKS4: 222 alive / 146 gold
- SOCKS5: 210 alive / 121 gold

## Historical pool

- Discovered: 109961
- Ever alive: 15389
- Ever gold: 496

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
