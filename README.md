# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 389
- HTTP: 112 alive / 63 gold
- HTTPS: 43 alive / 14 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 175416
- Ever alive: 33127
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
