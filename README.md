# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 400
- HTTP: 105 alive / 76 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 171 alive / 151 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48191
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
