# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 381
- HTTP: 92 alive / 56 gold
- HTTPS: 47 alive / 11 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 186 alive / 159 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33113
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
