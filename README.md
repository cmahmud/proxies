# SyndProxy validated proxy pool

## Current pool

- Alive now: 1613
- Gold now: 5
- HTTP: 702 alive / 5 gold
- HTTPS: 235 alive / 0 gold
- SOCKS4: 387 alive / 0 gold
- SOCKS5: 289 alive / 0 gold

## Historical pool

- Discovered: 169115
- Ever alive: 32654
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
