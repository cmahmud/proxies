# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 391
- HTTP: 110 alive / 66 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 171 alive / 152 gold
- SOCKS5: 182 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48086
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
