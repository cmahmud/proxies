# SyndProxy validated proxy pool

## Current pool

- Alive now: 678
- Gold now: 469
- HTTP: 165 alive / 95 gold
- HTTPS: 125 alive / 37 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 208 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45253
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
