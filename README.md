# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 390
- HTTP: 114 alive / 55 gold
- HTTPS: 50 alive / 11 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 196 alive / 165 gold

## Historical pool

- Discovered: 178001
- Ever alive: 33358
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
