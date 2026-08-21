# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 389
- HTTP: 280 alive / 78 gold
- HTTPS: 159 alive / 18 gold
- SOCKS4: 223 alive / 150 gold
- SOCKS5: 234 alive / 143 gold

## Historical pool

- Discovered: 156831
- Ever alive: 29631
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
