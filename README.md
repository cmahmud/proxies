# SyndProxy private pool

## Current pool

- Alive now: 745
- Gold now: 390
- HTTP: 178 alive / 84 gold
- HTTPS: 119 alive / 18 gold
- SOCKS4: 221 alive / 136 gold
- SOCKS5: 227 alive / 152 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29762
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
