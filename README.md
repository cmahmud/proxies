# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 488
- HTTP: 374 alive / 155 gold
- HTTPS: 274 alive / 87 gold
- SOCKS4: 180 alive / 116 gold
- SOCKS5: 193 alive / 130 gold

## Historical pool

- Discovered: 117177
- Ever alive: 17737
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
