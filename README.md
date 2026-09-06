# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 398
- HTTP: 106 alive / 78 gold
- HTTPS: 50 alive / 17 gold
- SOCKS4: 169 alive / 150 gold
- SOCKS5: 172 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48203
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
