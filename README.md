# SyndProxy validated proxy pool

## Current pool

- Alive now: 571
- Gold now: 458
- HTTP: 112 alive / 91 gold
- HTTPS: 98 alive / 34 gold
- SOCKS4: 167 alive / 163 gold
- SOCKS5: 194 alive / 170 gold

## Historical pool

- Discovered: 208020
- Ever alive: 45663
- Ever gold: 1437

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
