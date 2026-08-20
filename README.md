# SyndProxy private pool

## Current pool

- Alive now: 1770
- Gold now: 630
- HTTP: 645 alive / 224 gold
- HTTPS: 570 alive / 100 gold
- SOCKS4: 235 alive / 147 gold
- SOCKS5: 320 alive / 159 gold

## Historical pool

- Discovered: 142697
- Ever alive: 24313
- Ever gold: 982

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
