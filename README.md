# SyndProxy private pool

## Current pool

- Alive now: 1038
- Gold now: 464
- HTTP: 368 alive / 120 gold
- HTTPS: 284 alive / 87 gold
- SOCKS4: 212 alive / 141 gold
- SOCKS5: 174 alive / 116 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17464
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
