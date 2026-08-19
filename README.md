# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 482
- HTTP: 291 alive / 129 gold
- HTTPS: 236 alive / 84 gold
- SOCKS4: 204 alive / 127 gold
- SOCKS5: 221 alive / 142 gold

## Historical pool

- Discovered: 117147
- Ever alive: 17562
- Ever gold: 678

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
