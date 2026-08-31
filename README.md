# SyndProxy validated proxy pool

## Current pool

- Alive now: 604
- Gold now: 472
- HTTP: 134 alive / 99 gold
- HTTPS: 101 alive / 37 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45123
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
