# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 433
- HTTP: 122 alive / 81 gold
- HTTPS: 92 alive / 24 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34130
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
