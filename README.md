# SyndProxy validated proxy pool

## Current pool

- Alive now: 647
- Gold now: 473
- HTTP: 148 alive / 95 gold
- HTTPS: 129 alive / 39 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 196 alive / 178 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45185
- Ever gold: 1426

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
