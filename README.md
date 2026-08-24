# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 389
- HTTP: 91 alive / 53 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33346
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
