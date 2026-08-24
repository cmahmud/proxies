# SyndProxy validated proxy pool

## Current pool

- Alive now: 575
- Gold now: 401
- HTTP: 119 alive / 68 gold
- HTTPS: 53 alive / 11 gold
- SOCKS4: 192 alive / 158 gold
- SOCKS5: 211 alive / 164 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33333
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
