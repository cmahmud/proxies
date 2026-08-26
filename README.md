# SyndProxy validated proxy pool

## Current pool

- Alive now: 678
- Gold now: 404
- HTTP: 139 alive / 80 gold
- HTTPS: 191 alive / 25 gold
- SOCKS4: 170 alive / 146 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 190445
- Ever alive: 39963
- Ever gold: 1305

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
