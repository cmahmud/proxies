# SyndProxy validated proxy pool

## Current pool

- Alive now: 637
- Gold now: 474
- HTTP: 157 alive / 102 gold
- HTTPS: 120 alive / 36 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45204
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
