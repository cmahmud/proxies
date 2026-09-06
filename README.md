# SyndProxy validated proxy pool

## Current pool

- Alive now: 472
- Gold now: 385
- HTTP: 94 alive / 65 gold
- HTTPS: 38 alive / 16 gold
- SOCKS4: 169 alive / 154 gold
- SOCKS5: 171 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48187
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
