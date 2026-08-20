# SyndProxy private pool

## Current pool

- Alive now: 609
- Gold now: 385
- HTTP: 140 alive / 64 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 196 alive / 152 gold
- SOCKS5: 197 alive / 152 gold

## Historical pool

- Discovered: 146659
- Ever alive: 25710
- Ever gold: 1072

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
