# SyndProxy private pool

## Current pool

- Alive now: 864
- Gold now: 337
- HTTP: 281 alive / 80 gold
- HTTPS: 194 alive / 30 gold
- SOCKS4: 201 alive / 137 gold
- SOCKS5: 188 alive / 90 gold

## Historical pool

- Discovered: 167110
- Ever alive: 32514
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
