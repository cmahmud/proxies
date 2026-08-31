# SyndProxy validated proxy pool

## Current pool

- Alive now: 700
- Gold now: 473
- HTTP: 185 alive / 98 gold
- HTTPS: 114 alive / 37 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 229 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45292
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
