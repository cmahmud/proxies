# SyndProxy validated proxy pool

## Current pool

- Alive now: 617
- Gold now: 200
- HTTP: 185 alive / 43 gold
- HTTPS: 105 alive / 9 gold
- SOCKS4: 138 alive / 65 gold
- SOCKS5: 189 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32679
- Ever gold: 1195

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
