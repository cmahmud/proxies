# SyndProxy private pool

## Current pool

- Alive now: 1231
- Gold now: 529
- HTTP: 447 alive / 175 gold
- HTTPS: 345 alive / 57 gold
- SOCKS4: 229 alive / 150 gold
- SOCKS5: 210 alive / 147 gold

## Historical pool

- Discovered: 127332
- Ever alive: 19715
- Ever gold: 775

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
