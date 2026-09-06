# SyndProxy validated proxy pool

## Current pool

- Alive now: 434
- Gold now: 368
- HTTP: 68 alive / 56 gold
- HTTPS: 26 alive / 14 gold
- SOCKS4: 166 alive / 151 gold
- SOCKS5: 174 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48257
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
