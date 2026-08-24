# SyndProxy validated proxy pool

## Current pool

- Alive now: 558
- Gold now: 433
- HTTP: 108 alive / 79 gold
- HTTPS: 89 alive / 22 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34107
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
