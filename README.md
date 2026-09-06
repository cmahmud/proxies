# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 394
- HTTP: 109 alive / 73 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 167 alive / 151 gold
- SOCKS5: 183 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48100
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
