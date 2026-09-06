# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 402
- HTTP: 90 alive / 64 gold
- HTTPS: 31 alive / 16 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 189 alive / 165 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48250
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
