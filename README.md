# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 431
- HTTP: 123 alive / 88 gold
- HTTPS: 77 alive / 34 gold
- SOCKS4: 162 alive / 151 gold
- SOCKS5: 180 alive / 158 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44074
- Ever gold: 1396

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
