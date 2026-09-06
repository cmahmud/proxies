# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 395
- HTTP: 109 alive / 73 gold
- HTTPS: 37 alive / 15 gold
- SOCKS4: 170 alive / 151 gold
- SOCKS5: 182 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48222
- Ever gold: 1525

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
