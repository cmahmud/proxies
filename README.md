# SyndProxy validated proxy pool

## Current pool

- Alive now: 678
- Gold now: 472
- HTTP: 164 alive / 102 gold
- HTTPS: 139 alive / 35 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 200 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45161
- Ever gold: 1424

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
