# SyndProxy private pool

## Current pool

- Alive now: 814
- Gold now: 350
- HTTP: 235 alive / 77 gold
- HTTPS: 169 alive / 19 gold
- SOCKS4: 207 alive / 123 gold
- SOCKS5: 203 alive / 131 gold

## Historical pool

- Discovered: 157663
- Ever alive: 29788
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
