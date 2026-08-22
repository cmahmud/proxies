# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 403
- HTTP: 367 alive / 87 gold
- HTTPS: 235 alive / 24 gold
- SOCKS4: 227 alive / 149 gold
- SOCKS5: 254 alive / 143 gold

## Historical pool

- Discovered: 165751
- Ever alive: 32286
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
