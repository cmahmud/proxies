# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 391
- HTTP: 100 alive / 62 gold
- HTTPS: 37 alive / 12 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 184 alive / 158 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33316
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
