# SyndProxy private pool

## Current pool

- Alive now: 1655
- Gold now: 627
- HTTP: 644 alive / 236 gold
- HTTPS: 501 alive / 129 gold
- SOCKS4: 189 alive / 100 gold
- SOCKS5: 321 alive / 162 gold

## Historical pool

- Discovered: 142748
- Ever alive: 24669
- Ever gold: 1030

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
