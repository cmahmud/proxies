# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 387
- HTTP: 119 alive / 54 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 192 alive / 162 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33363
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
