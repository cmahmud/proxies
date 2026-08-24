# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 386
- HTTP: 110 alive / 55 gold
- HTTPS: 36 alive / 11 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 180 alive / 162 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33456
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
