# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 357
- HTTP: 72 alive / 39 gold
- HTTPS: 34 alive / 10 gold
- SOCKS4: 166 alive / 155 gold
- SOCKS5: 181 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48299
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
