# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 370
- HTTP: 74 alive / 53 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 170 alive / 154 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33047
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
