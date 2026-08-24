# SyndProxy validated proxy pool

## Current pool

- Alive now: 605
- Gold now: 437
- HTTP: 134 alive / 80 gold
- HTTPS: 100 alive / 24 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 194 alive / 172 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34547
- Ever gold: 1256

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
