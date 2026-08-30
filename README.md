# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 420
- HTTP: 110 alive / 73 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 163 alive / 161 gold
- SOCKS5: 198 alive / 166 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44474
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
