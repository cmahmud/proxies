# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 474
- HTTP: 139 alive / 100 gold
- HTTPS: 132 alive / 38 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 196 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45182
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
