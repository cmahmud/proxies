# SyndProxy private pool

## Current pool

- Alive now: 1308
- Gold now: 388
- HTTP: 450 alive / 86 gold
- HTTPS: 312 alive / 12 gold
- SOCKS4: 239 alive / 130 gold
- SOCKS5: 307 alive / 160 gold

## Historical pool

- Discovered: 133919
- Ever alive: 21437
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
