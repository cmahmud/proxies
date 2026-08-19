# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 484
- HTTP: 310 alive / 131 gold
- HTTPS: 242 alive / 84 gold
- SOCKS4: 211 alive / 127 gold
- SOCKS5: 221 alive / 142 gold

## Historical pool

- Discovered: 117147
- Ever alive: 17562
- Ever gold: 679

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
