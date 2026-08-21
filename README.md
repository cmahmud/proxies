# SyndProxy private pool

## Current pool

- Alive now: 1016
- Gold now: 430
- HTTP: 311 alive / 94 gold
- HTTPS: 177 alive / 24 gold
- SOCKS4: 247 alive / 147 gold
- SOCKS5: 281 alive / 165 gold

## Historical pool

- Discovered: 152749
- Ever alive: 28160
- Ever gold: 1107

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
