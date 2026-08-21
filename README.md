# SyndProxy private pool

## Current pool

- Alive now: 1157
- Gold now: 371
- HTTP: 412 alive / 100 gold
- HTTPS: 280 alive / 23 gold
- SOCKS4: 201 alive / 111 gold
- SOCKS5: 264 alive / 137 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28329
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
