# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 386
- HTTP: 101 alive / 55 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 195 alive / 165 gold

## Historical pool

- Discovered: 178697
- Ever alive: 33389
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
