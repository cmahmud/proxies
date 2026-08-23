# SyndProxy validated proxy pool

## Current pool

- Alive now: 583
- Gold now: 206
- HTTP: 161 alive / 45 gold
- HTTPS: 163 alive / 9 gold
- SOCKS4: 102 alive / 68 gold
- SOCKS5: 157 alive / 84 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32682
- Ever gold: 1197

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
