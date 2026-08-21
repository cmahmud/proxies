# SyndProxy private pool

## Current pool

- Alive now: 833
- Gold now: 389
- HTTP: 228 alive / 90 gold
- HTTPS: 204 alive / 19 gold
- SOCKS4: 191 alive / 134 gold
- SOCKS5: 210 alive / 146 gold

## Historical pool

- Discovered: 152167
- Ever alive: 27880
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
