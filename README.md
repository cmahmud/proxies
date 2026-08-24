# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 396
- HTTP: 117 alive / 64 gold
- HTTPS: 47 alive / 12 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 190 alive / 160 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33315
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
