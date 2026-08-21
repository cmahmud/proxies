# SyndProxy private pool

## Current pool

- Alive now: 971
- Gold now: 407
- HTTP: 283 alive / 94 gold
- HTTPS: 226 alive / 18 gold
- SOCKS4: 215 alive / 150 gold
- SOCKS5: 247 alive / 145 gold

## Historical pool

- Discovered: 155695
- Ever alive: 29262
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
