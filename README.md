# SyndProxy validated proxy pool

## Current pool

- Alive now: 679
- Gold now: 471
- HTTP: 162 alive / 97 gold
- HTTPS: 128 alive / 37 gold
- SOCKS4: 178 alive / 163 gold
- SOCKS5: 211 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45253
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
