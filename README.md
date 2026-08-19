# SyndProxy private pool

## Current pool

- Alive now: 941
- Gold now: 473
- HTTP: 303 alive / 135 gold
- HTTPS: 248 alive / 90 gold
- SOCKS4: 201 alive / 137 gold
- SOCKS5: 189 alive / 111 gold

## Historical pool

- Discovered: 117110
- Ever alive: 17343
- Ever gold: 663

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
