# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 372
- HTTP: 320 alive / 87 gold
- HTTPS: 196 alive / 25 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 227 alive / 124 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32354
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
