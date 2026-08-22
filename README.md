# SyndProxy private pool

## Current pool

- Alive now: 1002
- Gold now: 424
- HTTP: 305 alive / 88 gold
- HTTPS: 187 alive / 28 gold
- SOCKS4: 234 alive / 148 gold
- SOCKS5: 276 alive / 160 gold

## Historical pool

- Discovered: 164928
- Ever alive: 32176
- Ever gold: 1172

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
