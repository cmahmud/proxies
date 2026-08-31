# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 442
- HTTP: 124 alive / 79 gold
- HTTPS: 64 alive / 30 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 195 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45558
- Ever gold: 1436

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
