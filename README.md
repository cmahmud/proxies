# SyndProxy validated proxy pool

## Current pool

- Alive now: 708
- Gold now: 455
- HTTP: 156 alive / 91 gold
- HTTPS: 128 alive / 31 gold
- SOCKS4: 181 alive / 159 gold
- SOCKS5: 243 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45318
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
