# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 217
- HTTP: 201 alive / 55 gold
- HTTPS: 72 alive / 11 gold
- SOCKS4: 86 alive / 68 gold
- SOCKS5: 135 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32685
- Ever gold: 1204

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
