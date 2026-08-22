# SyndProxy private pool

## Current pool

- Alive now: 897
- Gold now: 449
- HTTP: 262 alive / 100 gold
- HTTPS: 171 alive / 27 gold
- SOCKS4: 223 alive / 157 gold
- SOCKS5: 241 alive / 165 gold

## Historical pool

- Discovered: 167121
- Ever alive: 32536
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
