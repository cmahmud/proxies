# SyndProxy validated proxy pool

## Current pool

- Alive now: 623
- Gold now: 465
- HTTP: 137 alive / 93 gold
- HTTPS: 113 alive / 38 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44859
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
