# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 425
- HTTP: 106 alive / 75 gold
- HTTPS: 61 alive / 25 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44524
- Ever gold: 1404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
