# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 391
- HTTP: 125 alive / 59 gold
- HTTPS: 54 alive / 11 gold
- SOCKS4: 177 alive / 158 gold
- SOCKS5: 202 alive / 163 gold

## Historical pool

- Discovered: 178292
- Ever alive: 33373
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
