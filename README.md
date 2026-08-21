# SyndProxy private pool

## Current pool

- Alive now: 827
- Gold now: 389
- HTTP: 232 alive / 75 gold
- HTTPS: 146 alive / 18 gold
- SOCKS4: 210 alive / 149 gold
- SOCKS5: 239 alive / 147 gold

## Historical pool

- Discovered: 156831
- Ever alive: 29631
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
