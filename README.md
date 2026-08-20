# SyndProxy private pool

## Current pool

- Alive now: 1572
- Gold now: 628
- HTTP: 616 alive / 230 gold
- HTTPS: 492 alive / 120 gold
- SOCKS4: 207 alive / 136 gold
- SOCKS5: 257 alive / 142 gold

## Historical pool

- Discovered: 142729
- Ever alive: 24581
- Ever gold: 1029

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
