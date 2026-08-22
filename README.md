# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 402
- HTTP: 309 alive / 92 gold
- HTTPS: 236 alive / 36 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 230 alive / 134 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31290
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
