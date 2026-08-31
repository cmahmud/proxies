# SyndProxy validated proxy pool

## Current pool

- Alive now: 536
- Gold now: 409
- HTTP: 98 alive / 56 gold
- HTTPS: 80 alive / 26 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45515
- Ever gold: 1435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
