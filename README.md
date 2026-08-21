# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 390
- HTTP: 287 alive / 93 gold
- HTTPS: 228 alive / 23 gold
- SOCKS4: 198 alive / 134 gold
- SOCKS5: 238 alive / 140 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27887
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
