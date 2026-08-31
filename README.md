# SyndProxy validated proxy pool

## Current pool

- Alive now: 680
- Gold now: 469
- HTTP: 167 alive / 96 gold
- HTTPS: 124 alive / 36 gold
- SOCKS4: 182 alive / 163 gold
- SOCKS5: 207 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45252
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
