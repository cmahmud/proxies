# SyndProxy validated proxy pool

## Current pool

- Alive now: 730
- Gold now: 471
- HTTP: 191 alive / 97 gold
- HTTPS: 125 alive / 35 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 236 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45295
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
