# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 391
- HTTP: 116 alive / 59 gold
- HTTPS: 62 alive / 14 gold
- SOCKS4: 173 alive / 157 gold
- SOCKS5: 180 alive / 161 gold

## Historical pool

- Discovered: 179921
- Ever alive: 33510
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
