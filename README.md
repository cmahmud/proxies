# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 391
- HTTP: 122 alive / 71 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 169 alive / 153 gold
- SOCKS5: 174 alive / 152 gold

## Historical pool

- Discovered: 176564
- Ever alive: 33250
- Ever gold: 1231

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
