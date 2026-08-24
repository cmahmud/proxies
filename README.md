# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 390
- HTTP: 99 alive / 61 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33318
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
