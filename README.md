# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 432
- HTTP: 104 alive / 76 gold
- HTTPS: 72 alive / 24 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 199 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34090
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
