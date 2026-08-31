# SyndProxy validated proxy pool

## Current pool

- Alive now: 658
- Gold now: 484
- HTTP: 160 alive / 105 gold
- HTTPS: 128 alive / 41 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 200 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45241
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
