# SyndProxy private pool

## Current pool

- Alive now: 656
- Gold now: 387
- HTTP: 159 alive / 63 gold
- HTTPS: 75 alive / 18 gold
- SOCKS4: 214 alive / 152 gold
- SOCKS5: 208 alive / 154 gold

## Historical pool

- Discovered: 146660
- Ever alive: 25716
- Ever gold: 1073

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
