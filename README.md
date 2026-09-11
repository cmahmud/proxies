# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 424
- HTTP: 92 alive / 72 gold
- HTTPS: 60 alive / 26 gold
- SOCKS4: 201 alive / 167 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 223440
- Ever alive: 49075
- Ever gold: 1571

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
