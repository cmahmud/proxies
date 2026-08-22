# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 372
- HTTP: 297 alive / 87 gold
- HTTPS: 185 alive / 24 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 223 alive / 125 gold

## Historical pool

- Discovered: 165832
- Ever alive: 32354
- Ever gold: 1178

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
