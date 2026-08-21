# SyndProxy private pool

## Current pool

- Alive now: 1018
- Gold now: 444
- HTTP: 324 alive / 113 gold
- HTTPS: 227 alive / 29 gold
- SOCKS4: 228 alive / 155 gold
- SOCKS5: 239 alive / 147 gold

## Historical pool

- Discovered: 160020
- Ever alive: 30531
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
