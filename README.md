# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 377
- HTTP: 95 alive / 53 gold
- HTTPS: 42 alive / 13 gold
- SOCKS4: 173 alive / 154 gold
- SOCKS5: 191 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33035
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
