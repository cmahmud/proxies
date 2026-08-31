# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 445
- HTTP: 139 alive / 79 gold
- HTTPS: 102 alive / 31 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 218 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45414
- Ever gold: 1431

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
