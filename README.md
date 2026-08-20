# SyndProxy private pool

## Current pool

- Alive now: 859
- Gold now: 372
- HTTP: 194 alive / 79 gold
- HTTPS: 265 alive / 20 gold
- SOCKS4: 200 alive / 135 gold
- SOCKS5: 200 alive / 138 gold

## Historical pool

- Discovered: 148776
- Ever alive: 26514
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
