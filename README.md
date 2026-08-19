# SyndProxy private pool

## Current pool

- Alive now: 1187
- Gold now: 578
- HTTP: 455 alive / 186 gold
- HTTPS: 317 alive / 118 gold
- SOCKS4: 211 alive / 131 gold
- SOCKS5: 204 alive / 143 gold

## Historical pool

- Discovered: 127340
- Ever alive: 19827
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
