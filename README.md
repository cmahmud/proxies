# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 409
- HTTP: 101 alive / 72 gold
- HTTPS: 32 alive / 17 gold
- SOCKS4: 171 alive / 154 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48247
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
