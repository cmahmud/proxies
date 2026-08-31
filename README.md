# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 421
- HTTP: 90 alive / 62 gold
- HTTPS: 74 alive / 28 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 190 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45489
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
