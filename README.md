# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 388
- HTTP: 118 alive / 68 gold
- HTTPS: 43 alive / 13 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 178 alive / 150 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33279
- Ever gold: 1233

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
