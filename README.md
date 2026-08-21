# SyndProxy private pool

## Current pool

- Alive now: 1075
- Gold now: 453
- HTTP: 367 alive / 100 gold
- HTTPS: 234 alive / 34 gold
- SOCKS4: 212 alive / 147 gold
- SOCKS5: 262 alive / 172 gold

## Historical pool

- Discovered: 153740
- Ever alive: 28712
- Ever gold: 1112

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
