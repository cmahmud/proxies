# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 385
- HTTP: 87 alive / 58 gold
- HTTPS: 48 alive / 12 gold
- SOCKS4: 175 alive / 155 gold
- SOCKS5: 183 alive / 160 gold

## Historical pool

- Discovered: 174830
- Ever alive: 33106
- Ever gold: 1226

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
