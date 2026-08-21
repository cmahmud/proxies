# SyndProxy private pool

## Current pool

- Alive now: 1149
- Gold now: 424
- HTTP: 409 alive / 109 gold
- HTTPS: 286 alive / 29 gold
- SOCKS4: 225 alive / 157 gold
- SOCKS5: 229 alive / 129 gold

## Historical pool

- Discovered: 153127
- Ever alive: 28440
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
