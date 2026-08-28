# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 393
- HTTP: 79 alive / 53 gold
- HTTPS: 36 alive / 15 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42844
- Ever gold: 1362

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
