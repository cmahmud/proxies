# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 415
- HTTP: 124 alive / 75 gold
- HTTPS: 81 alive / 19 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 181471
- Ever alive: 33762
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
