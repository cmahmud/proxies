# SyndProxy validated proxy pool

## Current pool

- Alive now: 674
- Gold now: 477
- HTTP: 154 alive / 100 gold
- HTTPS: 120 alive / 39 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 225 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45256
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
