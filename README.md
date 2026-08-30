# SyndProxy validated proxy pool

## Current pool

- Alive now: 634
- Gold now: 466
- HTTP: 135 alive / 92 gold
- HTTPS: 119 alive / 39 gold
- SOCKS4: 174 alive / 162 gold
- SOCKS5: 206 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44900
- Ever gold: 1418

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
