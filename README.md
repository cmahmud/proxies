# SyndProxy private pool

## Current pool

- Alive now: 863
- Gold now: 406
- HTTP: 279 alive / 93 gold
- HTTPS: 158 alive / 30 gold
- SOCKS4: 205 alive / 145 gold
- SOCKS5: 221 alive / 138 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32532
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
