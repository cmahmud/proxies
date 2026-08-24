# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 416
- HTTP: 121 alive / 76 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 162 alive / 159 gold
- SOCKS5: 189 alive / 162 gold

## Historical pool

- Discovered: 181471
- Ever alive: 33760
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
