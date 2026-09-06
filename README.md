# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 387
- HTTP: 109 alive / 71 gold
- HTTPS: 40 alive / 19 gold
- SOCKS4: 170 alive / 150 gold
- SOCKS5: 171 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48191
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
