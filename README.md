# SyndProxy validated proxy pool

## Current pool

- Alive now: 717
- Gold now: 469
- HTTP: 170 alive / 92 gold
- HTTPS: 128 alive / 38 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 246 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45280
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
