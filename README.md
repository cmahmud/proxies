# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 399
- HTTP: 106 alive / 74 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 182 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48235
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
