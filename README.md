# SyndProxy validated proxy pool

## Current pool

- Alive now: 621
- Gold now: 445
- HTTP: 122 alive / 78 gold
- HTTPS: 141 alive / 36 gold
- SOCKS4: 165 alive / 159 gold
- SOCKS5: 193 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44664
- Ever gold: 1409

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
