# SyndProxy validated proxy pool

## Current pool

- Alive now: 602
- Gold now: 416
- HTTP: 106 alive / 64 gold
- HTTPS: 139 alive / 23 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41300
- Ever gold: 1324

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
