# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 471
- HTTP: 155 alive / 101 gold
- HTTPS: 129 alive / 36 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 195 alive / 174 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45202
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
