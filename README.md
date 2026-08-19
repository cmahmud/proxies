# SyndProxy private pool

## Current pool

- Alive now: 1270
- Gold now: 392
- HTTP: 431 alive / 88 gold
- HTTPS: 284 alive / 14 gold
- SOCKS4: 242 alive / 129 gold
- SOCKS5: 313 alive / 161 gold

## Historical pool

- Discovered: 133919
- Ever alive: 21445
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
