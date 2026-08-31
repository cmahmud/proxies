# SyndProxy validated proxy pool

## Current pool

- Alive now: 563
- Gold now: 442
- HTTP: 118 alive / 77 gold
- HTTPS: 67 alive / 31 gold
- SOCKS4: 182 alive / 162 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45558
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
