# SyndProxy validated proxy pool

## Current pool

- Alive now: 449
- Gold now: 342
- HTTP: 76 alive / 52 gold
- HTTPS: 30 alive / 7 gold
- SOCKS4: 166 alive / 140 gold
- SOCKS5: 177 alive / 143 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48289
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
