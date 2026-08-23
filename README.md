# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 364
- HTTP: 97 alive / 45 gold
- HTTPS: 26 alive / 11 gold
- SOCKS4: 182 alive / 153 gold
- SOCKS5: 198 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33027
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
