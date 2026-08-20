# SyndProxy private pool

## Current pool

- Alive now: 1543
- Gold now: 657
- HTTP: 590 alive / 243 gold
- HTTPS: 483 alive / 134 gold
- SOCKS4: 209 alive / 136 gold
- SOCKS5: 261 alive / 144 gold

## Historical pool

- Discovered: 142729
- Ever alive: 24573
- Ever gold: 1028

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
