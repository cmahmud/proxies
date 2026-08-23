# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 386
- HTTP: 133 alive / 61 gold
- HTTPS: 52 alive / 13 gold
- SOCKS4: 167 alive / 153 gold
- SOCKS5: 190 alive / 159 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33145
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
