# SyndProxy validated proxy pool

## Current pool

- Alive now: 713
- Gold now: 455
- HTTP: 156 alive / 91 gold
- HTTPS: 131 alive / 30 gold
- SOCKS4: 182 alive / 159 gold
- SOCKS5: 244 alive / 175 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45318
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
