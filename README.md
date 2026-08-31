# SyndProxy validated proxy pool

## Current pool

- Alive now: 646
- Gold now: 475
- HTTP: 154 alive / 98 gold
- HTTPS: 122 alive / 38 gold
- SOCKS4: 180 alive / 163 gold
- SOCKS5: 190 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45248
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
