# SyndProxy private pool

## Current pool

- Alive now: 1692
- Gold now: 684
- HTTP: 657 alive / 264 gold
- HTTPS: 479 alive / 129 gold
- SOCKS4: 215 alive / 127 gold
- SOCKS5: 341 alive / 164 gold

## Historical pool

- Discovered: 143496
- Ever alive: 24833
- Ever gold: 1049

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
