# SyndProxy private pool

## Current pool

- Alive now: 989
- Gold now: 343
- HTTP: 309 alive / 48 gold
- HTTPS: 220 alive / 14 gold
- SOCKS4: 232 alive / 143 gold
- SOCKS5: 228 alive / 138 gold

## Historical pool

- Discovered: 107145
- Ever alive: 15097
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
