# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 473
- HTTP: 156 alive / 96 gold
- HTTPS: 123 alive / 38 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 198 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45187
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
