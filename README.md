# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 396
- HTTP: 113 alive / 77 gold
- HTTPS: 45 alive / 16 gold
- SOCKS4: 176 alive / 152 gold
- SOCKS5: 172 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48202
- Ever gold: 1523

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
