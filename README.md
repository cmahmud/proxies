# SyndProxy private pool

## Current pool

- Alive now: 1274
- Gold now: 403
- HTTP: 427 alive / 85 gold
- HTTPS: 277 alive / 17 gold
- SOCKS4: 245 alive / 149 gold
- SOCKS5: 325 alive / 152 gold

## Historical pool

- Discovered: 134540
- Ever alive: 21976
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
