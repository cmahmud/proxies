# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 439
- HTTP: 129 alive / 91 gold
- HTTPS: 70 alive / 36 gold
- SOCKS4: 157 alive / 152 gold
- SOCKS5: 176 alive / 160 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44090
- Ever gold: 1397

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
