# SyndProxy private pool

## Current pool

- Alive now: 1482
- Gold now: 656
- HTTP: 555 alive / 252 gold
- HTTPS: 417 alive / 118 gold
- SOCKS4: 206 alive / 126 gold
- SOCKS5: 304 alive / 160 gold

## Historical pool

- Discovered: 143487
- Ever alive: 24805
- Ever gold: 1047

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
