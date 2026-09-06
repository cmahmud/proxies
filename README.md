# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 399
- HTTP: 115 alive / 76 gold
- HTTPS: 64 alive / 21 gold
- SOCKS4: 165 alive / 146 gold
- SOCKS5: 181 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48057
- Ever gold: 1516

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
