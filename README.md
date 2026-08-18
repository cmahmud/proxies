# SyndProxy private pool

## Current pool

- Alive now: 849
- Gold now: 266
- HTTP: 236 alive / 33 gold
- HTTPS: 188 alive / 5 gold
- SOCKS4: 210 alive / 119 gold
- SOCKS5: 215 alive / 109 gold

## Historical pool

- Discovered: 99124
- Ever alive: 11877
- Ever gold: 389

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
