# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 385
- HTTP: 100 alive / 69 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 167 alive / 152 gold
- SOCKS5: 171 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48183
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
