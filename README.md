# SyndProxy private pool

## Current pool

- Alive now: 1043
- Gold now: 392
- HTTP: 325 alive / 98 gold
- HTTPS: 210 alive / 26 gold
- SOCKS4: 243 alive / 132 gold
- SOCKS5: 265 alive / 136 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25094
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
