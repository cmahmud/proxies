# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 344
- HTTP: 311 alive / 49 gold
- HTTPS: 226 alive / 14 gold
- SOCKS4: 234 alive / 143 gold
- SOCKS5: 228 alive / 138 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15097
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
