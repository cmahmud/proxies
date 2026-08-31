# SyndProxy validated proxy pool

## Current pool

- Alive now: 644
- Gold now: 475
- HTTP: 150 alive / 98 gold
- HTTPS: 123 alive / 39 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 195 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45184
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
