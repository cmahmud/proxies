# SyndProxy private pool

## Current pool

- Alive now: 1573
- Gold now: 590
- HTTP: 623 alive / 191 gold
- HTTPS: 475 alive / 85 gold
- SOCKS4: 226 alive / 144 gold
- SOCKS5: 249 alive / 170 gold

## Historical pool

- Discovered: 141227
- Ever alive: 23991
- Ever gold: 967

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
