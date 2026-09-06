# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 372
- HTTP: 78 alive / 53 gold
- HTTPS: 34 alive / 11 gold
- SOCKS4: 163 alive / 153 gold
- SOCKS5: 178 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48289
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
