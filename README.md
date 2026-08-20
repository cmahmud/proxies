# SyndProxy private pool

## Current pool

- Alive now: 661
- Gold now: 385
- HTTP: 167 alive / 68 gold
- HTTPS: 80 alive / 14 gold
- SOCKS4: 196 alive / 143 gold
- SOCKS5: 218 alive / 160 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25790
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
