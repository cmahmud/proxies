# SyndProxy private pool

## Current pool

- Alive now: 792
- Gold now: 385
- HTTP: 243 alive / 83 gold
- HTTPS: 107 alive / 16 gold
- SOCKS4: 203 alive / 136 gold
- SOCKS5: 239 alive / 150 gold

## Historical pool

- Discovered: 157428
- Ever alive: 29754
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
