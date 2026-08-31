# SyndProxy validated proxy pool

## Current pool

- Alive now: 612
- Gold now: 458
- HTTP: 123 alive / 89 gold
- HTTPS: 120 alive / 37 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45666
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
