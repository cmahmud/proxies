# SyndProxy private pool

## Current pool

- Alive now: 1365
- Gold now: 566
- HTTP: 544 alive / 179 gold
- HTTPS: 361 alive / 90 gold
- SOCKS4: 216 alive / 134 gold
- SOCKS5: 244 alive / 163 gold

## Historical pool

- Discovered: 138827
- Ever alive: 23068
- Ever gold: 913

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
