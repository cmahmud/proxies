# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 395
- HTTP: 97 alive / 60 gold
- HTTPS: 61 alive / 14 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33507
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
