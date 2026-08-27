# SyndProxy validated proxy pool

## Current pool

- Alive now: 640
- Gold now: 411
- HTTP: 119 alive / 65 gold
- HTTPS: 161 alive / 17 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 188 alive / 169 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40796
- Ever gold: 1312

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
