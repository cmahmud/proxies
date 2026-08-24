# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 438
- HTTP: 119 alive / 81 gold
- HTTPS: 65 alive / 25 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34162
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
