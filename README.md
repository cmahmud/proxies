# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 442
- HTTP: 140 alive / 79 gold
- HTTPS: 91 alive / 30 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 214 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45408
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
