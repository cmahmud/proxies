# SyndProxy private pool

## Current pool

- Alive now: 1645
- Gold now: 685
- HTTP: 620 alive / 265 gold
- HTTPS: 467 alive / 129 gold
- SOCKS4: 213 alive / 127 gold
- SOCKS5: 345 alive / 164 gold

## Historical pool

- Discovered: 143496
- Ever alive: 24824
- Ever gold: 1049

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
