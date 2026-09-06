# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 366
- HTTP: 78 alive / 51 gold
- HTTPS: 36 alive / 10 gold
- SOCKS4: 156 alive / 152 gold
- SOCKS5: 177 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48280
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
