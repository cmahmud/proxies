# SyndProxy private pool

## Current pool

- Alive now: 975
- Gold now: 405
- HTTP: 304 alive / 93 gold
- HTTPS: 193 alive / 24 gold
- SOCKS4: 230 alive / 143 gold
- SOCKS5: 248 alive / 145 gold

## Historical pool

- Discovered: 157419
- Ever alive: 29721
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
