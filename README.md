# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 382
- HTTP: 90 alive / 57 gold
- HTTPS: 45 alive / 10 gold
- SOCKS4: 174 alive / 156 gold
- SOCKS5: 187 alive / 159 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33113
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
