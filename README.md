# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 405
- HTTP: 98 alive / 63 gold
- HTTPS: 86 alive / 14 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39288
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
