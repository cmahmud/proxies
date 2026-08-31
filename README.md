# SyndProxy validated proxy pool

## Current pool

- Alive now: 594
- Gold now: 453
- HTTP: 125 alive / 85 gold
- HTTPS: 95 alive / 36 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 204 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45605
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
