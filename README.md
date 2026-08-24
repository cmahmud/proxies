# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 388
- HTTP: 101 alive / 61 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 190 alive / 157 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33316
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
