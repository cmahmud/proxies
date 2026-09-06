# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 393
- HTTP: 105 alive / 74 gold
- HTTPS: 39 alive / 16 gold
- SOCKS4: 168 alive / 151 gold
- SOCKS5: 175 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48193
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
