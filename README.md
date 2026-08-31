# SyndProxy validated proxy pool

## Current pool

- Alive now: 710
- Gold now: 471
- HTTP: 166 alive / 93 gold
- HTTPS: 129 alive / 38 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 241 alive / 179 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45280
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
