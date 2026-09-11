# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 347
- HTTP: 147 alive / 78 gold
- HTTPS: 84 alive / 30 gold
- SOCKS4: 165 alive / 61 gold
- SOCKS5: 267 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48574
- Ever gold: 1546

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
