# SyndProxy validated proxy pool

## Current pool

- Alive now: 555
- Gold now: 441
- HTTP: 123 alive / 85 gold
- HTTPS: 77 alive / 29 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44295
- Ever gold: 1398

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
