# SyndProxy validated proxy pool

## Current pool

- Alive now: 641
- Gold now: 473
- HTTP: 154 alive / 99 gold
- HTTPS: 122 alive / 37 gold
- SOCKS4: 170 alive / 161 gold
- SOCKS5: 195 alive / 176 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45190
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
