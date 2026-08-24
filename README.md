# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 374
- HTTP: 125 alive / 51 gold
- HTTPS: 41 alive / 7 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 191 alive / 160 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33449
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
