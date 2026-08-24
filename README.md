# SyndProxy validated proxy pool

## Current pool

- Alive now: 588
- Gold now: 438
- HTTP: 139 alive / 86 gold
- HTTPS: 83 alive / 19 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34427
- Ever gold: 1255

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
