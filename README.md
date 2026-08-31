# SyndProxy validated proxy pool

## Current pool

- Alive now: 611
- Gold now: 473
- HTTP: 139 alive / 100 gold
- HTTPS: 102 alive / 37 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45123
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
