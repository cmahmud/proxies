# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 438
- HTTP: 117 alive / 81 gold
- HTTPS: 81 alive / 25 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 188 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34156
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
