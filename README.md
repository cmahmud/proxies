# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 404
- HTTP: 108 alive / 62 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 192 alive / 167 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33680
- Ever gold: 1248

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
