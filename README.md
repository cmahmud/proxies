# SyndProxy validated proxy pool

## Current pool

- Alive now: 577
- Gold now: 435
- HTTP: 131 alive / 82 gold
- HTTPS: 89 alive / 22 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 188 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33990
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
