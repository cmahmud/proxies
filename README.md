# SyndProxy validated proxy pool

## Current pool

- Alive now: 608
- Gold now: 432
- HTTP: 131 alive / 79 gold
- HTTPS: 88 alive / 24 gold
- SOCKS4: 198 alive / 161 gold
- SOCKS5: 191 alive / 168 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34081
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
