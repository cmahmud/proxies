# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 405
- HTTP: 196 alive / 72 gold
- HTTPS: 82 alive / 15 gold
- SOCKS4: 190 alive / 156 gold
- SOCKS5: 206 alive / 162 gold

## Historical pool

- Discovered: 177315
- Ever alive: 33302
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
