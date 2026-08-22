# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 403
- HTTP: 373 alive / 85 gold
- HTTPS: 229 alive / 26 gold
- SOCKS4: 229 alive / 148 gold
- SOCKS5: 254 alive / 144 gold

## Historical pool

- Discovered: 165502
- Ever alive: 32281
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
