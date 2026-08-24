# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 439
- HTTP: 118 alive / 82 gold
- HTTPS: 72 alive / 25 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 187 alive / 171 gold

## Historical pool

- Discovered: 181856
- Ever alive: 34165
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
