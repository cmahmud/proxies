# SyndProxy private pool

## Current pool

- Alive now: 1073
- Gold now: 222
- HTTP: 527 alive / 35 gold
- HTTPS: 193 alive / 9 gold
- SOCKS4: 162 alive / 105 gold
- SOCKS5: 191 alive / 73 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6206
- Ever gold: 294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
