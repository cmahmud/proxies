# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 395
- HTTP: 96 alive / 60 gold
- HTTPS: 57 alive / 14 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 176 alive / 162 gold

## Historical pool

- Discovered: 179712
- Ever alive: 33507
- Ever gold: 1239

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
