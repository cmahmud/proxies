# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 391
- HTTP: 124 alive / 58 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 203 alive / 164 gold

## Historical pool

- Discovered: 178292
- Ever alive: 33373
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
