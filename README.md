# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 391
- HTTP: 138 alive / 58 gold
- HTTPS: 64 alive / 14 gold
- SOCKS4: 179 alive / 157 gold
- SOCKS5: 190 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33527
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
