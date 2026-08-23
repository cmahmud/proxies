# SyndProxy validated proxy pool

## Current pool

- Alive now: 449
- Gold now: 371
- HTTP: 89 alive / 48 gold
- HTTPS: 26 alive / 13 gold
- SOCKS4: 164 alive / 154 gold
- SOCKS5: 170 alive / 156 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
