# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 434
- HTTP: 326 alive / 93 gold
- HTTPS: 234 alive / 31 gold
- SOCKS4: 227 alive / 145 gold
- SOCKS5: 260 alive / 165 gold

## Historical pool

- Discovered: 158917
- Ever alive: 30133
- Ever gold: 1141

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
