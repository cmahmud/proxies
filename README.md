# SyndProxy private pool

## Current pool

- Alive now: 822
- Gold now: 403
- HTTP: 244 alive / 93 gold
- HTTPS: 156 alive / 30 gold
- SOCKS4: 203 alive / 144 gold
- SOCKS5: 219 alive / 136 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32532
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
