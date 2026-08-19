# SyndProxy private pool

## Current pool

- Alive now: 1308
- Gold now: 389
- HTTP: 464 alive / 94 gold
- HTTPS: 321 alive / 21 gold
- SOCKS4: 219 alive / 130 gold
- SOCKS5: 304 alive / 144 gold

## Historical pool

- Discovered: 134553
- Ever alive: 22122
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
