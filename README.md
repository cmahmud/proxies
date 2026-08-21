# SyndProxy private pool

## Current pool

- Alive now: 1023
- Gold now: 431
- HTTP: 318 alive / 94 gold
- HTTPS: 221 alive / 28 gold
- SOCKS4: 219 alive / 145 gold
- SOCKS5: 265 alive / 164 gold

## Historical pool

- Discovered: 158917
- Ever alive: 30123
- Ever gold: 1141

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
