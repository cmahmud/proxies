# SyndProxy private pool

## Current pool

- Alive now: 950
- Gold now: 409
- HTTP: 278 alive / 83 gold
- HTTPS: 199 alive / 18 gold
- SOCKS4: 236 alive / 161 gold
- SOCKS5: 237 alive / 147 gold

## Historical pool

- Discovered: 158244
- Ever alive: 30023
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
