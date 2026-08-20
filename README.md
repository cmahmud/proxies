# SyndProxy private pool

## Current pool

- Alive now: 1642
- Gold now: 610
- HTTP: 639 alive / 215 gold
- HTTPS: 540 alive / 116 gold
- SOCKS4: 218 alive / 134 gold
- SOCKS5: 245 alive / 145 gold

## Historical pool

- Discovered: 141137
- Ever alive: 23840
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
