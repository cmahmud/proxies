# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 357
- HTTP: 342 alive / 67 gold
- HTTPS: 189 alive / 16 gold
- SOCKS4: 226 alive / 145 gold
- SOCKS5: 231 alive / 129 gold

## Historical pool

- Discovered: 111009
- Ever alive: 16109
- Ever gold: 507

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
