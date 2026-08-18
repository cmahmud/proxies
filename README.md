# SyndProxy private pool

## Current pool

- Alive now: 701
- Gold now: 250
- HTTP: 253 alive / 27 gold
- HTTPS: 88 alive / 10 gold
- SOCKS4: 181 alive / 127 gold
- SOCKS5: 179 alive / 86 gold

## Historical pool

- Discovered: 94350
- Ever alive: 9794
- Ever gold: 376

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
