# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 463
- HTTP: 137 alive / 92 gold
- HTTPS: 112 alive / 38 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 201 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44859
- Ever gold: 1417

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
