# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 403
- HTTP: 99 alive / 64 gold
- HTTPS: 100 alive / 12 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 184 alive / 165 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43049
- Ever gold: 1365

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
