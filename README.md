# SyndProxy validated proxy pool

## Current pool

- Alive now: 455
- Gold now: 371
- HTTP: 87 alive / 49 gold
- HTTPS: 30 alive / 13 gold
- SOCKS4: 166 alive / 154 gold
- SOCKS5: 172 alive / 155 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
