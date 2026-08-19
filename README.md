# SyndProxy private pool

## Current pool

- Alive now: 1033
- Gold now: 464
- HTTP: 362 alive / 120 gold
- HTTPS: 285 alive / 87 gold
- SOCKS4: 211 alive / 141 gold
- SOCKS5: 175 alive / 116 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17464
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
