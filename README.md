# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 400
- HTTP: 82 alive / 58 gold
- HTTPS: 73 alive / 20 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42746
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
