# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 426
- HTTP: 129 alive / 84 gold
- HTTPS: 77 alive / 31 gold
- SOCKS4: 159 alive / 150 gold
- SOCKS5: 185 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44056
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
