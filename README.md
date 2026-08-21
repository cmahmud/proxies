# SyndProxy private pool

## Current pool

- Alive now: 963
- Gold now: 415
- HTTP: 345 alive / 110 gold
- HTTPS: 184 alive / 28 gold
- SOCKS4: 202 alive / 131 gold
- SOCKS5: 232 alive / 146 gold

## Historical pool

- Discovered: 160212
- Ever alive: 30628
- Ever gold: 1146

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
