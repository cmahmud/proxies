# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 384
- HTTP: 105 alive / 71 gold
- HTTPS: 41 alive / 17 gold
- SOCKS4: 167 alive / 149 gold
- SOCKS5: 178 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48192
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
