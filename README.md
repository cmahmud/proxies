# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 370
- HTTP: 70 alive / 52 gold
- HTTPS: 34 alive / 12 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 180 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48302
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
