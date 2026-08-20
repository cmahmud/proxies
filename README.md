# SyndProxy private pool

## Current pool

- Alive now: 647
- Gold now: 354
- HTTP: 171 alive / 71 gold
- HTTPS: 107 alive / 18 gold
- SOCKS4: 191 alive / 131 gold
- SOCKS5: 178 alive / 134 gold

## Historical pool

- Discovered: 147169
- Ever alive: 25783
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
