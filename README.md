# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 386
- HTTP: 118 alive / 54 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 195 alive / 162 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33363
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
