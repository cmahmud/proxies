# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 204
- HTTP: 239 alive / 43 gold
- HTTPS: 57 alive / 6 gold
- SOCKS4: 96 alive / 67 gold
- SOCKS5: 149 alive / 88 gold

## Historical pool

- Discovered: 170278
- Ever alive: 32741
- Ever gold: 1207

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
