# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 372
- HTTP: 101 alive / 50 gold
- HTTPS: 31 alive / 11 gold
- SOCKS4: 178 alive / 154 gold
- SOCKS5: 194 alive / 157 gold

## Historical pool

- Discovered: 173755
- Ever alive: 33025
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
