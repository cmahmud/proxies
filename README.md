# SyndProxy private pool

## Current pool

- Alive now: 1565
- Gold now: 613
- HTTP: 548 alive / 212 gold
- HTTPS: 448 alive / 116 gold
- SOCKS4: 225 alive / 149 gold
- SOCKS5: 344 alive / 136 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23692
- Ever gold: 956

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
