# SyndProxy validated proxy pool

## Current pool

- Alive now: 652
- Gold now: 475
- HTTP: 160 alive / 98 gold
- HTTPS: 121 alive / 38 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 197 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45187
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
