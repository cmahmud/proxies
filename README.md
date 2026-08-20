# SyndProxy private pool

## Current pool

- Alive now: 1613
- Gold now: 586
- HTTP: 586 alive / 196 gold
- HTTPS: 475 alive / 99 gold
- SOCKS4: 242 alive / 141 gold
- SOCKS5: 310 alive / 150 gold

## Historical pool

- Discovered: 138944
- Ever alive: 23374
- Ever gold: 918

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
