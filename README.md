# SyndProxy validated proxy pool

## Current pool

- Alive now: 446
- Gold now: 222
- HTTP: 176 alive / 61 gold
- HTTPS: 57 alive / 11 gold
- SOCKS4: 82 alive / 66 gold
- SOCKS5: 131 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32686
- Ever gold: 1205

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
