# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 442
- HTTP: 134 alive / 86 gold
- HTTPS: 97 alive / 23 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 198 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34386
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
