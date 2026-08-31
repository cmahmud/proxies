# SyndProxy validated proxy pool

## Current pool

- Alive now: 662
- Gold now: 481
- HTTP: 162 alive / 105 gold
- HTTPS: 129 alive / 39 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 196 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45245
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
