# SyndProxy private pool

## Current pool

- Alive now: 1748
- Gold now: 700
- HTTP: 656 alive / 232 gold
- HTTPS: 538 alive / 144 gold
- SOCKS4: 239 alive / 158 gold
- SOCKS5: 315 alive / 166 gold

## Historical pool

- Discovered: 142702
- Ever alive: 24369
- Ever gold: 1021

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
