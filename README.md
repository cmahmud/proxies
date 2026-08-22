# SyndProxy private pool

## Current pool

- Alive now: 1121
- Gold now: 418
- HTTP: 423 alive / 94 gold
- HTTPS: 226 alive / 32 gold
- SOCKS4: 221 alive / 132 gold
- SOCKS5: 251 alive / 160 gold

## Historical pool

- Discovered: 162773
- Ever alive: 31670
- Ever gold: 1164

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
