# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 386
- HTTP: 103 alive / 58 gold
- HTTPS: 40 alive / 8 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 187 alive / 161 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33319
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
