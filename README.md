# SyndProxy private pool

## Current pool

- Alive now: 1337
- Gold now: 233
- HTTP: 617 alive / 31 gold
- HTTPS: 250 alive / 9 gold
- SOCKS4: 236 alive / 109 gold
- SOCKS5: 234 alive / 84 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 335

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
