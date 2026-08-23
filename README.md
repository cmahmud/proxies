# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 382
- HTTP: 90 alive / 58 gold
- HTTPS: 44 alive / 11 gold
- SOCKS4: 165 alive / 154 gold
- SOCKS5: 188 alive / 159 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33114
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
