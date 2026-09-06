# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 403
- HTTP: 104 alive / 76 gold
- HTTPS: 39 alive / 17 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 170 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48189
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
