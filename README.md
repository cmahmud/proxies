# SyndProxy validated proxy pool

## Current pool

- Alive now: 574
- Gold now: 386
- HTTP: 118 alive / 64 gold
- HTTPS: 83 alive / 11 gold
- SOCKS4: 177 alive / 153 gold
- SOCKS5: 196 alive / 158 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33143
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
