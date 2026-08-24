# SyndProxy validated proxy pool

## Current pool

- Alive now: 537
- Gold now: 391
- HTTP: 110 alive / 57 gold
- HTTPS: 61 alive / 13 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33530
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
