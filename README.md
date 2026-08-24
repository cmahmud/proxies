# SyndProxy validated proxy pool

## Current pool

- Alive now: 567
- Gold now: 431
- HTTP: 111 alive / 78 gold
- HTTPS: 58 alive / 24 gold
- SOCKS4: 195 alive / 161 gold
- SOCKS5: 203 alive / 168 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34081
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
