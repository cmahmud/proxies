# SyndProxy validated proxy pool

## Current pool

- Alive now: 561
- Gold now: 434
- HTTP: 110 alive / 77 gold
- HTTPS: 75 alive / 24 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 198 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34090
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
