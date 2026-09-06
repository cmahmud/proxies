# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 399
- HTTP: 110 alive / 71 gold
- HTTPS: 65 alive / 20 gold
- SOCKS4: 172 alive / 151 gold
- SOCKS5: 182 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48086
- Ever gold: 1518

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
