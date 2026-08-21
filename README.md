# SyndProxy private pool

## Current pool

- Alive now: 791
- Gold now: 420
- HTTP: 229 alive / 94 gold
- HTTPS: 129 alive / 28 gold
- SOCKS4: 194 alive / 139 gold
- SOCKS5: 239 alive / 159 gold

## Historical pool

- Discovered: 155807
- Ever alive: 29413
- Ever gold: 1126

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
