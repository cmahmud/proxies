# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 386
- HTTP: 97 alive / 70 gold
- HTTPS: 42 alive / 14 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 171 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48180
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
