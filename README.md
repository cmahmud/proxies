# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 279
- HTTP: 322 alive / 28 gold
- HTTPS: 217 alive / 7 gold
- SOCKS4: 243 alive / 123 gold
- SOCKS5: 233 alive / 121 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13168
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
