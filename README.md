# SyndProxy private pool

## Current pool

- Alive now: 1055
- Gold now: 422
- HTTP: 354 alive / 83 gold
- HTTPS: 219 alive / 29 gold
- SOCKS4: 223 alive / 139 gold
- SOCKS5: 259 alive / 171 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32237
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
