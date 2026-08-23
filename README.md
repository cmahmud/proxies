# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 385
- HTTP: 133 alive / 60 gold
- HTTPS: 53 alive / 13 gold
- SOCKS4: 166 alive / 153 gold
- SOCKS5: 187 alive / 159 gold

## Historical pool

- Discovered: 175427
- Ever alive: 33145
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
