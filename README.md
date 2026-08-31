# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 487
- HTTP: 151 alive / 102 gold
- HTTPS: 139 alive / 46 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 198 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44998
- Ever gold: 1422

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
