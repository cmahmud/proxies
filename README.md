# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 406
- HTTP: 107 alive / 62 gold
- HTTPS: 91 alive / 13 gold
- SOCKS4: 179 alive / 162 gold
- SOCKS5: 194 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39299
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
