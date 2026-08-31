# SyndProxy validated proxy pool

## Current pool

- Alive now: 624
- Gold now: 461
- HTTP: 152 alive / 94 gold
- HTTPS: 113 alive / 36 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45143
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
