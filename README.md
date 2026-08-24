# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 439
- HTTP: 122 alive / 83 gold
- HTTPS: 92 alive / 25 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 34000
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
