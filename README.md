# SyndProxy validated proxy pool

## Current pool

- Alive now: 606
- Gold now: 391
- HTTP: 188 alive / 63 gold
- HTTPS: 48 alive / 15 gold
- SOCKS4: 177 alive / 154 gold
- SOCKS5: 193 alive / 159 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33137
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
