# SyndProxy private pool

## Current pool

- Alive now: 1027
- Gold now: 489
- HTTP: 352 alive / 141 gold
- HTTPS: 272 alive / 93 gold
- SOCKS4: 204 alive / 138 gold
- SOCKS5: 199 alive / 117 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17339
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
