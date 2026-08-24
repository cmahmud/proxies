# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 385
- HTTP: 105 alive / 55 gold
- HTTPS: 41 alive / 9 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 183 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33535
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
