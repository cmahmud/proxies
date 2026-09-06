# SyndProxy validated proxy pool

## Current pool

- Alive now: 435
- Gold now: 365
- HTTP: 70 alive / 55 gold
- HTTPS: 26 alive / 12 gold
- SOCKS4: 164 alive / 151 gold
- SOCKS5: 175 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48257
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
