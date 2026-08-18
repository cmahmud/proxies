# SyndProxy private pool

## Current pool

- Alive now: 830
- Gold now: 262
- HTTP: 217 alive / 32 gold
- HTTPS: 188 alive / 4 gold
- SOCKS4: 220 alive / 129 gold
- SOCKS5: 205 alive / 97 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10663
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
