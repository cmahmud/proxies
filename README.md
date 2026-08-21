# SyndProxy private pool

## Current pool

- Alive now: 750
- Gold now: 387
- HTTP: 194 alive / 85 gold
- HTTPS: 124 alive / 25 gold
- SOCKS4: 204 alive / 134 gold
- SOCKS5: 228 alive / 143 gold

## Historical pool

- Discovered: 154725
- Ever alive: 29157
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
