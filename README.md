# SyndProxy private pool

## Current pool

- Alive now: 1193
- Gold now: 541
- HTTP: 450 alive / 188 gold
- HTTPS: 319 alive / 82 gold
- SOCKS4: 215 alive / 129 gold
- SOCKS5: 209 alive / 142 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19827
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
