# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 374
- HTTP: 342 alive / 84 gold
- HTTPS: 264 alive / 24 gold
- SOCKS4: 169 alive / 115 gold
- SOCKS5: 223 alive / 151 gold

## Historical pool

- Discovered: 158226
- Ever alive: 29890
- Ever gold: 1138

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
