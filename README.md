# SyndProxy private pool

## Current pool

- Alive now: 1036
- Gold now: 404
- HTTP: 379 alive / 92 gold
- HTTPS: 236 alive / 34 gold
- SOCKS4: 191 alive / 124 gold
- SOCKS5: 230 alive / 154 gold

## Historical pool

- Discovered: 163242
- Ever alive: 31703
- Ever gold: 1165

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
