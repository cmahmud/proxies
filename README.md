# SyndProxy private pool

## Current pool

- Alive now: 875
- Gold now: 409
- HTTP: 272 alive / 89 gold
- HTTPS: 172 alive / 23 gold
- SOCKS4: 201 alive / 142 gold
- SOCKS5: 230 alive / 155 gold

## Historical pool

- Discovered: 156414
- Ever alive: 29451
- Ever gold: 1127

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
