# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 391
- HTTP: 129 alive / 59 gold
- HTTPS: 67 alive / 14 gold
- SOCKS4: 173 alive / 156 gold
- SOCKS5: 191 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33527
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
