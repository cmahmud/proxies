# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 508
- HTTP: 357 alive / 157 gold
- HTTPS: 277 alive / 91 gold
- SOCKS4: 218 alive / 142 gold
- SOCKS5: 206 alive / 118 gold

## Historical pool

- Discovered: 119842
- Ever alive: 18369
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
