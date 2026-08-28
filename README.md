# SyndProxy validated proxy pool

## Current pool

- Alive now: 471
- Gold now: 391
- HTTP: 73 alive / 56 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42844
- Ever gold: 1363

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
