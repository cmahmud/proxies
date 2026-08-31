# SyndProxy validated proxy pool

## Current pool

- Alive now: 691
- Gold now: 453
- HTTP: 153 alive / 90 gold
- HTTPS: 119 alive / 30 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 240 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45320
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
