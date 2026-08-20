# SyndProxy private pool

## Current pool

- Alive now: 1583
- Gold now: 645
- HTTP: 629 alive / 240 gold
- HTTPS: 488 alive / 129 gold
- SOCKS4: 207 alive / 133 gold
- SOCKS5: 259 alive / 143 gold

## Historical pool

- Discovered: 142728
- Ever alive: 24550
- Ever gold: 1028

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
