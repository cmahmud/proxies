# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 381
- HTTP: 76 alive / 56 gold
- HTTPS: 51 alive / 8 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 169 alive / 161 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43490
- Ever gold: 1372

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
