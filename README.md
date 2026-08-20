# SyndProxy private pool

## Current pool

- Alive now: 627
- Gold now: 385
- HTTP: 140 alive / 63 gold
- HTTPS: 71 alive / 14 gold
- SOCKS4: 199 alive / 153 gold
- SOCKS5: 217 alive / 155 gold

## Historical pool

- Discovered: 146662
- Ever alive: 25718
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
