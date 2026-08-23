# SyndProxy validated proxy pool

## Current pool

- Alive now: 382
- Gold now: 218
- HTTP: 140 alive / 56 gold
- HTTPS: 50 alive / 12 gold
- SOCKS4: 73 alive / 68 gold
- SOCKS5: 119 alive / 82 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32689
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
