# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 413
- HTTP: 121 alive / 73 gold
- HTTPS: 73 alive / 19 gold
- SOCKS4: 163 alive / 159 gold
- SOCKS5: 187 alive / 162 gold

## Historical pool

- Discovered: 181088
- Ever alive: 33755
- Ever gold: 1250

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
