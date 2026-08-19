# SyndProxy private pool

## Current pool

- Alive now: 894
- Gold now: 342
- HTTP: 284 alive / 59 gold
- HTTPS: 191 alive / 15 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 205 alive / 128 gold

## Historical pool

- Discovered: 129236
- Ever alive: 20046
- Ever gold: 863

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
