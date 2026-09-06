# SyndProxy validated proxy pool

## Current pool

- Alive now: 481
- Gold now: 389
- HTTP: 105 alive / 73 gold
- HTTPS: 40 alive / 17 gold
- SOCKS4: 169 alive / 152 gold
- SOCKS5: 167 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48191
- Ever gold: 1522

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
