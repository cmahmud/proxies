# SyndProxy private pool

## Current pool

- Alive now: 1584
- Gold now: 569
- HTTP: 659 alive / 209 gold
- HTTPS: 506 alive / 94 gold
- SOCKS4: 177 alive / 104 gold
- SOCKS5: 242 alive / 162 gold

## Historical pool

- Discovered: 143428
- Ever alive: 24742
- Ever gold: 1037

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
