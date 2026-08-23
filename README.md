# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 365
- HTTP: 87 alive / 46 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 173 alive / 153 gold
- SOCKS5: 191 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33027
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
