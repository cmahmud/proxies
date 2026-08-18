# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 276
- HTTP: 320 alive / 27 gold
- HTTPS: 214 alive / 7 gold
- SOCKS4: 240 alive / 122 gold
- SOCKS5: 229 alive / 120 gold

## Historical pool

- Discovered: 102840
- Ever alive: 13168
- Ever gold: 415

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
