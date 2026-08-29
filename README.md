# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 399
- HTTP: 98 alive / 70 gold
- HTTPS: 80 alive / 17 gold
- SOCKS4: 160 alive / 152 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43296
- Ever gold: 1369

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
