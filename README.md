# SyndProxy private pool

## Current pool

- Alive now: 854
- Gold now: 401
- HTTP: 254 alive / 91 gold
- HTTPS: 174 alive / 29 gold
- SOCKS4: 201 alive / 144 gold
- SOCKS5: 225 alive / 137 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32532
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
