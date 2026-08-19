# SyndProxy private pool

## Current pool

- Alive now: 1177
- Gold now: 422
- HTTP: 394 alive / 88 gold
- HTTPS: 259 alive / 13 gold
- SOCKS4: 253 alive / 157 gold
- SOCKS5: 271 alive / 164 gold

## Historical pool

- Discovered: 131718
- Ever alive: 20744
- Ever gold: 875

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
