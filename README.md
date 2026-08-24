# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 429
- HTTP: 120 alive / 78 gold
- HTTPS: 74 alive / 22 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 189 alive / 169 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34116
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
