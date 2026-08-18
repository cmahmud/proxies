# SyndProxy private pool

## Current pool

- Alive now: 677
- Gold now: 259
- HTTP: 152 alive / 29 gold
- HTTPS: 94 alive / 6 gold
- SOCKS4: 223 alive / 131 gold
- SOCKS5: 208 alive / 93 gold

## Historical pool

- Discovered: 91741
- Ever alive: 9108
- Ever gold: 362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
