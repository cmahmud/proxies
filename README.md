# SyndProxy private pool

## Current pool

- Alive now: 1006
- Gold now: 403
- HTTP: 340 alive / 85 gold
- HTTPS: 196 alive / 25 gold
- SOCKS4: 221 alive / 146 gold
- SOCKS5: 249 alive / 147 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29717
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
