# SyndProxy private pool

## Current pool

- Alive now: 1025
- Gold now: 407
- HTTP: 356 alive / 76 gold
- HTTPS: 225 alive / 20 gold
- SOCKS4: 216 alive / 157 gold
- SOCKS5: 228 alive / 154 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26805
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
