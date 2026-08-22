# SyndProxy private pool

## Current pool

- Alive now: 929
- Gold now: 417
- HTTP: 285 alive / 83 gold
- HTTPS: 187 alive / 29 gold
- SOCKS4: 211 alive / 143 gold
- SOCKS5: 246 alive / 162 gold

## Historical pool

- Discovered: 162746
- Ever alive: 31508
- Ever gold: 1160

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
