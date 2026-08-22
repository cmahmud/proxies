# SyndProxy private pool

## Current pool

- Alive now: 978
- Gold now: 427
- HTTP: 258 alive / 85 gold
- HTTPS: 223 alive / 29 gold
- SOCKS4: 215 alive / 143 gold
- SOCKS5: 282 alive / 170 gold

## Historical pool

- Discovered: 164944
- Ever alive: 32209
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
