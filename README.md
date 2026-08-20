# SyndProxy private pool

## Current pool

- Alive now: 1652
- Gold now: 625
- HTTP: 589 alive / 210 gold
- HTTPS: 457 alive / 117 gold
- SOCKS4: 236 alive / 144 gold
- SOCKS5: 370 alive / 154 gold

## Historical pool

- Discovered: 141229
- Ever alive: 24078
- Ever gold: 969

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
