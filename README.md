# SyndProxy validated proxy pool

## Current pool

- Alive now: 552
- Gold now: 439
- HTTP: 123 alive / 84 gold
- HTTPS: 76 alive / 24 gold
- SOCKS4: 168 alive / 161 gold
- SOCKS5: 185 alive / 170 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34231
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
