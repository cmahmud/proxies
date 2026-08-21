# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 415
- HTTP: 329 alive / 111 gold
- HTTPS: 200 alive / 27 gold
- SOCKS4: 209 alive / 132 gold
- SOCKS5: 231 alive / 145 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30643
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
