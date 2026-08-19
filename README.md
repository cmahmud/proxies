# SyndProxy private pool

## Current pool

- Alive now: 1090
- Gold now: 521
- HTTP: 403 alive / 159 gold
- HTTPS: 284 alive / 88 gold
- SOCKS4: 208 alive / 141 gold
- SOCKS5: 195 alive / 133 gold

## Historical pool

- Discovered: 119849
- Ever alive: 18489
- Ever gold: 719

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
