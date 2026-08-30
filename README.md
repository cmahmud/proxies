# SyndProxy validated proxy pool

## Current pool

- Alive now: 620
- Gold now: 471
- HTTP: 133 alive / 96 gold
- HTTPS: 117 alive / 41 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44920
- Ever gold: 1419

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
