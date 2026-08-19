# SyndProxy private pool

## Current pool

- Alive now: 1246
- Gold now: 406
- HTTP: 414 alive / 79 gold
- HTTPS: 274 alive / 15 gold
- SOCKS4: 290 alive / 149 gold
- SOCKS5: 268 alive / 163 gold

## Historical pool

- Discovered: 131116
- Ever alive: 20664
- Ever gold: 871

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
