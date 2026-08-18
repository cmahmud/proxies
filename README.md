# SyndProxy private pool

## Current pool

- Alive now: 692
- Gold now: 254
- HTTP: 172 alive / 30 gold
- HTTPS: 114 alive / 8 gold
- SOCKS4: 194 alive / 113 gold
- SOCKS5: 212 alive / 103 gold

## Historical pool

- Discovered: 95261
- Ever alive: 10225
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
