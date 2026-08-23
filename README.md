# SyndProxy validated proxy pool

## Current pool

- Alive now: 538
- Gold now: 385
- HTTP: 113 alive / 65 gold
- HTTPS: 50 alive / 11 gold
- SOCKS4: 166 alive / 152 gold
- SOCKS5: 209 alive / 157 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33144
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
