# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 382
- HTTP: 97 alive / 61 gold
- HTTPS: 37 alive / 11 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 195 alive / 154 gold

## Historical pool

- Discovered: 174803
- Ever alive: 33091
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
