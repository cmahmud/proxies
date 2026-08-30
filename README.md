# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 420
- HTTP: 106 alive / 70 gold
- HTTPS: 61 alive / 22 gold
- SOCKS4: 165 alive / 161 gold
- SOCKS5: 203 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44463
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
