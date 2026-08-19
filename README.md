# SyndProxy private pool

## Current pool

- Alive now: 1173
- Gold now: 556
- HTTP: 441 alive / 186 gold
- HTTPS: 317 alive / 98 gold
- SOCKS4: 209 alive / 129 gold
- SOCKS5: 206 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19827
- Ever gold: 801

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
