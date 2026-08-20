# SyndProxy private pool

## Current pool

- Alive now: 832
- Gold now: 382
- HTTP: 223 alive / 77 gold
- HTTPS: 203 alive / 20 gold
- SOCKS4: 201 alive / 147 gold
- SOCKS5: 205 alive / 138 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26828
- Ever gold: 1088

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
