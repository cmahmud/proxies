# SyndProxy validated proxy pool

## Current pool

- Alive now: 710
- Gold now: 469
- HTTP: 163 alive / 92 gold
- HTTPS: 136 alive / 38 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 239 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45280
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
