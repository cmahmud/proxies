# SyndProxy private pool

## Current pool

- Alive now: 1005
- Gold now: 314
- HTTP: 368 alive / 39 gold
- HTTPS: 170 alive / 11 gold
- SOCKS4: 238 alive / 137 gold
- SOCKS5: 229 alive / 127 gold

## Historical pool

- Discovered: 107043
- Ever alive: 14376
- Ever gold: 441

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
