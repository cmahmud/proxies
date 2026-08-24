# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 389
- HTTP: 99 alive / 55 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 188 alive / 163 gold

## Historical pool

- Discovered: 177985
- Ever alive: 33357
- Ever gold: 1234

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
