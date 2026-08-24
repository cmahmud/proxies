# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 381
- HTTP: 123 alive / 57 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 175 alive / 158 gold
- SOCKS5: 187 alive / 157 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33326
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
