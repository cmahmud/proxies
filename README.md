# SyndProxy private pool

## Current pool

- Alive now: 753
- Gold now: 410
- HTTP: 201 alive / 90 gold
- HTTPS: 124 alive / 26 gold
- SOCKS4: 189 alive / 138 gold
- SOCKS5: 239 alive / 156 gold

## Historical pool

- Discovered: 163841
- Ever alive: 31914
- Ever gold: 1169

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
