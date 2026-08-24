# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 434
- HTTP: 139 alive / 77 gold
- HTTPS: 95 alive / 25 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34646
- Ever gold: 1257

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
