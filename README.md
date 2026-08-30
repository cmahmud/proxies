# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 427
- HTTP: 129 alive / 84 gold
- HTTPS: 77 alive / 32 gold
- SOCKS4: 158 alive / 150 gold
- SOCKS5: 184 alive / 161 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44056
- Ever gold: 1393

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
