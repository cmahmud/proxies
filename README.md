# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 395
- HTTP: 94 alive / 60 gold
- HTTPS: 62 alive / 14 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 175 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33507
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
