# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 438
- HTTP: 123 alive / 83 gold
- HTTPS: 74 alive / 24 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34228
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
