# SyndProxy private pool

## Current pool

- Alive now: 1212
- Gold now: 443
- HTTP: 433 alive / 103 gold
- HTTPS: 241 alive / 28 gold
- SOCKS4: 263 alive / 152 gold
- SOCKS5: 275 alive / 160 gold

## Historical pool

- Discovered: 159282
- Ever alive: 30438
- Ever gold: 1145

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
