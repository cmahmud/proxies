# SyndProxy private pool

## Current pool

- Alive now: 1019
- Gold now: 283
- HTTP: 354 alive / 28 gold
- HTTPS: 181 alive / 6 gold
- SOCKS4: 245 alive / 125 gold
- SOCKS5: 239 alive / 124 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13135
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
