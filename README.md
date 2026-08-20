# SyndProxy private pool

## Current pool

- Alive now: 1683
- Gold now: 628
- HTTP: 647 alive / 237 gold
- HTTPS: 521 alive / 129 gold
- SOCKS4: 195 alive / 99 gold
- SOCKS5: 320 alive / 163 gold

## Historical pool

- Discovered: 142748
- Ever alive: 24667
- Ever gold: 1030

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
