# SyndProxy validated proxy pool

## Current pool

- Alive now: 404
- Gold now: 221
- HTTP: 153 alive / 60 gold
- HTTPS: 52 alive / 11 gold
- SOCKS4: 77 alive / 68 gold
- SOCKS5: 122 alive / 82 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32686
- Ever gold: 1205

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
