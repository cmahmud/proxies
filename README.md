# SyndProxy validated proxy pool

## Current pool

- Alive now: 706
- Gold now: 471
- HTTP: 158 alive / 95 gold
- HTTPS: 145 alive / 37 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 229 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45264
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
