# SyndProxy validated proxy pool

## Current pool

- Alive now: 670
- Gold now: 469
- HTTP: 160 alive / 100 gold
- HTTPS: 133 alive / 34 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 201 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45173
- Ever gold: 1425

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
