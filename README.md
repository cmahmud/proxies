# SyndProxy private pool

## Current pool

- Alive now: 889
- Gold now: 398
- HTTP: 285 alive / 90 gold
- HTTPS: 178 alive / 28 gold
- SOCKS4: 204 alive / 143 gold
- SOCKS5: 222 alive / 137 gold

## Historical pool

- Discovered: 167119
- Ever alive: 32532
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
