# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 362
- HTTP: 74 alive / 45 gold
- HTTPS: 33 alive / 10 gold
- SOCKS4: 165 alive / 155 gold
- SOCKS5: 181 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48299
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
