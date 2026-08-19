# SyndProxy private pool

## Current pool

- Alive now: 1048
- Gold now: 460
- HTTP: 341 alive / 121 gold
- HTTPS: 241 alive / 72 gold
- SOCKS4: 228 alive / 137 gold
- SOCKS5: 238 alive / 130 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16780
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
