# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 442
- HTTP: 139 alive / 82 gold
- HTTPS: 64 alive / 28 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 199830
- Ever alive: 43695
- Ever gold: 1379

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
