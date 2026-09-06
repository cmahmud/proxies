# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 385
- HTTP: 97 alive / 68 gold
- HTTPS: 41 alive / 15 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 175 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48177
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
