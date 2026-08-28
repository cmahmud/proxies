# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 404
- HTTP: 71 alive / 56 gold
- HTTPS: 61 alive / 23 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42778
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
