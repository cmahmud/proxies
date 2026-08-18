# SyndProxy private pool

## Current pool

- Alive now: 840
- Gold now: 262
- HTTP: 215 alive / 32 gold
- HTTPS: 200 alive / 4 gold
- SOCKS4: 221 alive / 129 gold
- SOCKS5: 204 alive / 97 gold

## Historical pool

- Discovered: 95396
- Ever alive: 10662
- Ever gold: 378

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
