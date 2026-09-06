# SyndProxy validated proxy pool

## Current pool

- Alive now: 477
- Gold now: 398
- HTTP: 87 alive / 61 gold
- HTTPS: 34 alive / 15 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48253
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
