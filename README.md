# SyndProxy validated proxy pool

## Current pool

- Alive now: 614
- Gold now: 197
- HTTP: 168 alive / 42 gold
- HTTPS: 167 alive / 9 gold
- SOCKS4: 111 alive / 65 gold
- SOCKS5: 168 alive / 81 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32682
- Ever gold: 1196

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
