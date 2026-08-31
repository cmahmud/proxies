# SyndProxy validated proxy pool

## Current pool

- Alive now: 699
- Gold now: 471
- HTTP: 173 alive / 96 gold
- HTTPS: 129 alive / 36 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 224 alive / 177 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45288
- Ever gold: 1428

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
