# SyndProxy validated proxy pool

## Current pool

- Alive now: 654
- Gold now: 469
- HTTP: 159 alive / 95 gold
- HTTPS: 118 alive / 35 gold
- SOCKS4: 180 alive / 164 gold
- SOCKS5: 197 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45249
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
