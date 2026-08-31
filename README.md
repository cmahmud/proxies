# SyndProxy validated proxy pool

## Current pool

- Alive now: 688
- Gold now: 454
- HTTP: 151 alive / 91 gold
- HTTPS: 119 alive / 30 gold
- SOCKS4: 179 alive / 159 gold
- SOCKS5: 239 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45318
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
