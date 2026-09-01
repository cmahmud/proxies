# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 427
- HTTP: 92 alive / 71 gold
- HTTPS: 57 alive / 26 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47030
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
