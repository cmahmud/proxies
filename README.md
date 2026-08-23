# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 335
- HTTP: 113 alive / 35 gold
- HTTPS: 51 alive / 10 gold
- SOCKS4: 162 alive / 149 gold
- SOCKS5: 175 alive / 141 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32787
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
