# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 420
- HTTP: 110 alive / 74 gold
- HTTPS: 48 alive / 20 gold
- SOCKS4: 164 alive / 161 gold
- SOCKS5: 198 alive / 165 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44474
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
