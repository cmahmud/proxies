# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 422
- HTTP: 97 alive / 61 gold
- HTTPS: 68 alive / 31 gold
- SOCKS4: 186 alive / 162 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45494
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
