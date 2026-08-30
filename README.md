# SyndProxy validated proxy pool

## Current pool

- Alive now: 628
- Gold now: 465
- HTTP: 139 alive / 93 gold
- HTTPS: 111 alive / 37 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 205 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44858
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
