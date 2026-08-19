# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 489
- HTTP: 372 alive / 141 gold
- HTTPS: 281 alive / 93 gold
- SOCKS4: 211 alive / 137 gold
- SOCKS5: 219 alive / 118 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17339
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
