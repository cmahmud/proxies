# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 432
- HTTP: 108 alive / 78 gold
- HTTPS: 75 alive / 22 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34108
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
