# SyndProxy private pool

## Current pool

- Alive now: 947
- Gold now: 429
- HTTP: 291 alive / 106 gold
- HTTPS: 189 alive / 32 gold
- SOCKS4: 230 alive / 152 gold
- SOCKS5: 237 alive / 139 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30754
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
