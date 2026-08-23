# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 381
- HTTP: 114 alive / 64 gold
- HTTPS: 42 alive / 10 gold
- SOCKS4: 159 alive / 152 gold
- SOCKS5: 173 alive / 155 gold

## Historical pool

- Discovered: 174154
- Ever alive: 33071
- Ever gold: 1224

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
