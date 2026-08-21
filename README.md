# SyndProxy private pool

## Current pool

- Alive now: 1032
- Gold now: 428
- HTTP: 338 alive / 85 gold
- HTTPS: 207 alive / 28 gold
- SOCKS4: 223 alive / 155 gold
- SOCKS5: 264 alive / 160 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30227
- Ever gold: 1143

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
