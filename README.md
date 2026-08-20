# SyndProxy private pool

## Current pool

- Alive now: 1907
- Gold now: 642
- HTTP: 738 alive / 230 gold
- HTTPS: 597 alive / 101 gold
- SOCKS4: 248 alive / 148 gold
- SOCKS5: 324 alive / 163 gold

## Historical pool

- Discovered: 142698
- Ever alive: 24337
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
