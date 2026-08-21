# SyndProxy private pool

## Current pool

- Alive now: 1024
- Gold now: 429
- HTTP: 322 alive / 91 gold
- HTTPS: 237 alive / 32 gold
- SOCKS4: 219 alive / 154 gold
- SOCKS5: 246 alive / 152 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30241
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
