# SyndProxy private pool

## Current pool

- Alive now: 932
- Gold now: 291
- HTTP: 268 alive / 46 gold
- HTTPS: 222 alive / 8 gold
- SOCKS4: 221 alive / 112 gold
- SOCKS5: 221 alive / 125 gold

## Historical pool

- Discovered: 107048
- Ever alive: 14488
- Ever gold: 465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
