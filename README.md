# SyndProxy private pool

## Current pool

- Alive now: 1761
- Gold now: 686
- HTTP: 658 alive / 234 gold
- HTTPS: 540 alive / 123 gold
- SOCKS4: 245 alive / 158 gold
- SOCKS5: 318 alive / 171 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24363
- Ever gold: 996

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
