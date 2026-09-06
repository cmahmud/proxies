# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 400
- HTTP: 103 alive / 77 gold
- HTTPS: 40 alive / 19 gold
- SOCKS4: 165 alive / 151 gold
- SOCKS5: 175 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48192
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
