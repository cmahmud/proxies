# SyndProxy private pool

## Current pool

- Alive now: 1012
- Gold now: 279
- HTTP: 319 alive / 28 gold
- HTTPS: 228 alive / 7 gold
- SOCKS4: 238 alive / 123 gold
- SOCKS5: 227 alive / 121 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13174
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
