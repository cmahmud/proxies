# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 385
- HTTP: 121 alive / 54 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 195 alive / 161 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33363
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
