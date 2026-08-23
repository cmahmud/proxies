# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 333
- HTTP: 113 alive / 35 gold
- HTTPS: 52 alive / 10 gold
- SOCKS4: 162 alive / 148 gold
- SOCKS5: 173 alive / 140 gold

## Historical pool

- Discovered: 170572
- Ever alive: 32787
- Ever gold: 1212

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
