# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 412
- HTTP: 101 alive / 72 gold
- HTTPS: 79 alive / 15 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34829
- Ever gold: 1258

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
