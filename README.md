# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 381
- HTTP: 91 alive / 53 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 172 alive / 154 gold
- SOCKS5: 193 alive / 162 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33346
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
