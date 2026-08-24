# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 390
- HTTP: 103 alive / 60 gold
- HTTPS: 37 alive / 10 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33319
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
